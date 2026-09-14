from app import config
from app.rag.documents import load_files
from app.rag.splitters import split_into_chunks
from app.rag.vectorstore import store_vectors_in_chromadb,count_vectors
from app.rag.embeddings import embedding_documents


def main():

    documents = load_files(config.PATH_DOCUMENTS_FILES)

    chunks = split_into_chunks(documents)

    # Toujours un seul chunk pour le test
    #test_chunk = chunks[:1]

    vectors = embedding_documents(chunks)

    ids = [f"doc_{i}" for i in range(len(chunks))]

    response = store_vectors_in_chromadb(
        chunks,
        vectors,
        ids
    )

    print(response)
    collection=count_vectors()

    print("Nombre de documents dans Chroma :", collection)
if __name__ == "__main__":
    main()