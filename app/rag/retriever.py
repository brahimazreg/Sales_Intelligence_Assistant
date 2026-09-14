from app import config
import chromadb
from app.rag.embeddings import embedding_question

chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(
    name="rag_collection_sales"
)

def retrive_question(question, top_k):

    vector_question = embedding_question(question)

    results = collection.query(
        query_embeddings=[vector_question],
        n_results=top_k
    )

    documents = results["documents"][0]

    return documents
# transform documents into context
def build_context(documents):
    context = "\n\n".join(documents)

    return context