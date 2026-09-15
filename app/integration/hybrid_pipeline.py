from app.schema import extract_schema
from app.rag.retriever import retrieve_question
from app.integration.generator_with_rag import generate_sql_with_rag
from app.validator import validate_sql, validate_table, validate_column
from app.connection import execute_query
from app.integration.rag_pipeline import build_context
from app import config


def question_to_hybrid(question):

    # 1. Récupérer le schéma MySQL
    schema = extract_schema()

    # 2. Récupérer le contexte métier depuis Chroma
    documents = retrieve_question(
        question,
        config.TOP_K_RESULT
    )

    # 3. Construire le contexte
    context = build_context(documents)

    # 4. Générer le SQL avec question + schéma + contexte métier
    sql_generated = generate_sql_with_rag(
        question=question,
        schema=schema,
        context=context
    )

    # 5. Afficher le SQL généré
    print("\n--- SQL GÉNÉRÉ ---")
    print(sql_generated)
    print("--- FIN SQL ---\n")

    # 6. Valider le SQL
    validate_sql(sql_generated)
    validate_table(sql_generated, schema)
    validate_column(sql_generated, schema)

    # 7. Exécuter la requête
    result = execute_query(sql_generated)

    return result

# just for test
if __name__ == "__main__":

    question = "Quelle est la marge totale en excluant les commandes annulées ?"

    result = question_to_hybrid(question)

    print("\n--- RÉSULTAT HYBRID ---")
    print(result)
    print("\n--- VALEURS ---")
    print(result.to_string(index=False))
    print("\n--- DICT ---")
    print(result.to_dict(orient="records"))
    print("--- FIN RÉSULTAT ---")