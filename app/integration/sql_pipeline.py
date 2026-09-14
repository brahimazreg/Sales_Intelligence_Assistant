from app.schema import extract_schema
from app.integration.generator_with_rag import generate_sql_with_rag
from app.validator import validate_sql, validate_table, validate_column
from app.connection import execute_query


def question_to_sql(question):

    # 1. Récupérer le schéma MySQL
    schema = extract_schema()

    # 2. Générer le SQL
    sql_generated = generate_sql_with_rag(
        question=question,
        schema=schema,
        context=""
    )

    # 3. Afficher le SQL
    print("\n--- SQL GÉNÉRÉ ---")
    print(sql_generated)
    print("--- FIN SQL ---\n")

    # 4. Valider le SQL
    validate_sql(sql_generated)
    validate_table(sql_generated, schema)
    validate_column(sql_generated, schema)

    # 5. Exécuter la requête
    result = execute_query(sql_generated)

    return result

# just pour test
if __name__ == "__main__":

    question = "Quel est le chiffre d'affaires par client"

    result = question_to_sql(question)

    print("\nRésultat :")

    for row in result:
        print(row)