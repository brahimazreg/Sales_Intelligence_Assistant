from app import config
import chromadb
from app.rag.embeddings import embedding_question

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(
    name="rag_collection_sales"
)

def retrieve_question(question, top_k):

    vector_question = embedding_question(question)

    results = collection.query(
        query_embeddings=[vector_question],
        n_results=top_k
    )

    documents = results["documents"][0]

    print("\n--- DOCUMENTS RÉCUPÉRÉS ---")

    for i, document in enumerate(documents, 1):
        print(f"\nDOCUMENT {i}:")
        print(document)

    print("\n--- FIN DOCUMENTS ---\n")

    return documents