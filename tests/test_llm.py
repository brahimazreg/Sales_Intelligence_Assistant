from app.llm import get_llm


def main():
    llm = get_llm()

    print("Test Ollama...")

    response = llm.invoke(
        "Réponds uniquement par : OK"
    )

    print("Réponse :")
    print(response.content)


if __name__ == "__main__":
    main()