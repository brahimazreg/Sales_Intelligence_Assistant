from app.rag.retriever import retrive_question , build_context
from app import config


def main():
    question="Quel est le chiffre d'affaires total ?"
    documents =retrive_question(question ,config.TOP_K_RESULT)
    response = build_context(documents)
    print(response)

if __name__ == "__main__":
    main()