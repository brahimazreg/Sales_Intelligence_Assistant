from app.rag.retriever import retrive_question, build_context
from app.integration.generator_rag import generate_rag_answer
from app import config


def question_to_rag(question):

    # 1. Récupérer les documents depuis Chroma
    documents = retrive_question(
        question,
        config.TOP_K_RESULT
    )

    # 2. Construire le contexte
    context = build_context(documents)

    # 3. Générer la réponse
    answer = generate_rag_answer(
        question=question,
        context=context
    )

    return answer


if __name__ == "__main__":

    question = "Quelle est la définition du chiffre d'affaires ?"

    answer = question_to_rag(question)

    print("\n--- RÉPONSE RAG ---")
    print(answer)
    print("--- FIN RÉPONSE ---")