from app.router.router import route_question
from app.integration.sql_pipeline import question_to_sql
from app.integration.rag_pipeline import question_to_rag
from app.integration.hybrid_pipeline import question_to_hybrid


def test_question(question):
    print("\n" + "=" * 70)
    print(f"QUESTION : {question}")
    print("=" * 70)

    # 1. ROUTAGE
    route = route_question(question)

    print("\n--- ROUTE ---")
    print(route)

    # 2. EXÉCUTION
    print("\n--- TRAITEMENT ---")

    if route == "SQL":
        result = question_to_sql(question)

    elif route == "RAG":
        result = question_to_rag(question)

    elif route == "HYBRID":
        result = question_to_hybrid(question)

    else:
        raise ValueError(f"Route inconnue : {route}")

    # 3. RÉSULTAT
    print("\n--- RÉSULTAT ---")
    print(result)

    if hasattr(result, "columns"):
        print("\n--- COLONNES ---")
        print(list(result.columns))

    print("\n" + "=" * 70)


if __name__ == "__main__":
    question = "Quels sont les produits à réapprovisionner ?"
    test_question(question)