from app.router.router import route_question
from app.integration.sql_pipeline import question_to_sql
from app.integration.rag_pipeline import question_to_rag
from app.integration.hybrid_pipeline import question_to_hybrid

def process_question(question):

    route = route_question(question)

    print("\n--- ROUTE ---")
    print(route)
    print("--- FIN ROUTE ---\n")

    if route == "SQL":
        return question_to_sql(question)

    if route == "RAG":
        return question_to_rag(question)

    if route == "HYBRID":
        return question_to_hybrid(question)

    raise ValueError(
        f"Route non gérée pour le moment : {route}"
    )


if __name__ == "__main__":

    questions = [
        "Quel est le chiffre d'affaires par client",
        "Quelle est la définition du chiffre d'affaires",
        "Quelle est la marge totale en excluant les commandes annulées ?"
    ]

    for question in questions:

        print("\n==============================")
        print("QUESTION :", question)
        print("==============================")

        result = process_question(question)

        print("\n--- RÉSULTAT ---")

        if isinstance(result, list):
            for row in result:
                print(row)
        else:
            print(result)