from app.schema import extract_schema
from app.rag.retriever import retrive_question
from app.integration.generator_with_rag import generate_sql_with_rag
from app.validator import validate_sql, validate_table, validate_column
from app.connection import execute_query
from app import config


def question_to_sql_with_rag(question):

    # 1. Récupérer le schéma MySQL
    schema = extract_schema()

    # 2. Récupérer le contexte métier depuis le RAG
    documents = retrive_question(
        question,
        config.TOP_K_RESULT
    )

    # 3. Construire le contexte
    context = "\n\n".join(documents)

    # 4. Générer le SQL avec question + schema + contexte RAG
    sql_generated = generate_sql_with_rag(
        question=question,
        schema=schema,
        context=context
    )

    # 5. Valider le SQL
    print("\n--- SQL GÉNÉRÉ ---")
    print(sql_generated)
    print("--- FIN SQL ---\n")
    validate_sql(sql_generated)
    validate_table(sql_generated, schema)
    validate_column(sql_generated, schema)

    # 6. Exécuter la requête
    result = execute_query(sql_generated)

    return result


if __name__ == "__main__":

    question = "Quel est le chiffre d'affaires par client"
    #question = "Quel est le meilleur produit"
    #question = "Quelle  est la marge totale"
    #question = "Quelles sont les  commandes annulées / exclusion des commandes annulées"
    #question = "Quels sont les produits à réapprovisionner"

    result = question_to_sql_with_rag(question)

    print("\nRésultat :")

    for row in result:
        print(row)