from langchain_ollama import OllamaEmbeddings


embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)


def embedding_documents(chunks):
    texts = [chunk.page_content for chunk in chunks]

    vectors = embedding_model.embed_documents(texts)

    return vectors


def embedding_question(question):
    vector_question=embedding_model.embed_query(question)

    return vector_question