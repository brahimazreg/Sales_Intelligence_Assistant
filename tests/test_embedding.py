from app.rag.documents import load_files
from app.rag.embeddings import embedding_documents
from app.rag.splitters import split_into_chunks
from app import config


def main():
    documents=load_files(config.PATH_DOCUMENTS_FILES)
    chunks = split_into_chunks(documents)

    print("Nombre de chunks :", len(chunks))

    # Pour l'instant, on teste seulement 1 chunk
    test_chunk = chunks[:1]

    vectors = embedding_documents(test_chunk)

    print("Embedding généré !")
    print("Nombre de vecteurs :", len(vectors))
    print("Dimension du vecteur :", len(vectors[0]))
    print("Premiers éléments :", vectors[0][:5])


if __name__ == "__main__":
    main()