import re

from app.schema import extract_schema
from app.integration.generator_with_rag import generate_sql_with_rag
from app.validator import validate_sql, validate_table, validate_column
from app.connection import execute_query


def clean_sql_response(response: str) -> str:
    """
    Extrait uniquement le SQL de la réponse du LLM.

    Gère :
    - ```sql ... ```
    - ``` ... ```
    - SQL brut
    - explications Markdown après le SQL
    """

    if not response or not response.strip():
        raise ValueError("La réponse SQL du LLM est vide")

    response = response.strip()

    # ---------------------------------------------------------
    # 1. Cas idéal : bloc Markdown ```sql ... ```
    # ---------------------------------------------------------
    match = re.search(
        r"```(?:sql|mysql)?\s*(.*?)```",
        response,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if match:
        sql = match.group(1).strip()
    else:
        sql = response

    # ---------------------------------------------------------
    # 2. Si le LLM a ajouté une explication après le SQL
    # ---------------------------------------------------------
    # Exemple :
    #
    # SELECT ...
    #
    # ---
    #
    # ### Explication
    #
    # On garde uniquement ce qui est avant ---
    #
    if "\n---" in sql:
        sql = sql.split("\n---", 1)[0].strip()

    # ---------------------------------------------------------
    # 3. Supprimer les éventuels titres Markdown
    # ---------------------------------------------------------
    sql = re.sub(
        r"^###.*?\n",
        "",
        sql,
        count=1,
        flags=re.IGNORECASE | re.DOTALL,
    ).strip()

    # ---------------------------------------------------------
    # 4. Garder jusqu'au dernier ;
    # ---------------------------------------------------------
    # Cela permet de supprimer une éventuelle explication
    # située après la requête.
    #
    # Exemple :
    # SELECT ...
    # ;
    # Voici l'explication...
    #
    last_semicolon = sql.rfind(";")

    if last_semicolon != -1:
        sql = sql[:last_semicolon + 1]

    sql = sql.strip()

    if not sql:
        raise ValueError("Impossible d'extraire le SQL de la réponse du LLM")

    return sql


def question_to_sql(question):

    # 1. Récupérer le schéma MySQL
    schema = extract_schema()

    # 2. Générer le SQL
    sql_generated = generate_sql_with_rag(
        question=question,
        schema=schema,
        context=""
    )

    # 3. Nettoyer la réponse du LLM
    sql_clean = clean_sql_response(sql_generated)

    # 4. Afficher le SQL nettoyé
    print("\n--- SQL GÉNÉRÉ ---")
    print(sql_clean)
    print("--- FIN SQL ---\n")

    print("=" * 80)
    print("RÉPONSE BRUTE DU LLM :")
    print(repr(sql_generated))
    print("=" * 80)

    print("=" * 80)
    print("SQL NETTOYÉ :")
    print(repr(sql_clean))
    print("=" * 80)

    # 5. Valider le SQL
    validate_sql(sql_clean)
    validate_table(sql_clean, schema)
    validate_column(sql_clean, schema)

    # 6. Exécuter la requête
    result = execute_query(sql_clean)

    return result


# Juste pour test
if __name__ == "__main__":

    question = "Quel est le chiffre d'affaires par client"

    result = question_to_sql(question)

    print("\nRésultat :")

    for row in result:
        print(row)