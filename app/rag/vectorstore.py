import chromadb


chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(
    name="rag_collection_sales"
)


def store_vectors_in_chromadb(chunks, vectors, ids):
    """
    Stocke les chunks et leurs embeddings dans ChromaDB.
    """

    documents = [chunk.page_content for chunk in chunks]

    collection.add(
        documents=documents,
        embeddings=vectors,
        ids=ids
    )

    return "Vectors saved in ChromaDB"

def count_vectors():
    return collection.count()