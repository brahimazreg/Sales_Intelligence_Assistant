
from app.rag.retriever import retrieve_question
from app.integration.generator_rag import generate_rag_answer
from app import config


def build_context(documents):
    """
    Transforme les documents récupérés par Chroma
    en un seul contexte texte pour le LLM.
    """
    return "\n\n--- DOCUMENT ---\n\n".join(documents)


def question_to_rag(question):

    # 1. Récupérer les documents depuis Chroma
    documents = retrieve_question(
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

