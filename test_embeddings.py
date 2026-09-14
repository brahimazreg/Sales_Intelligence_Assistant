from app.rag.embeddings import get_embeddings


embeddings = get_embeddings()

text = "Le chiffre d'affaires exclut les commandes annulées."

vector = embeddings.embed_query(text)

print("Embedding généré !")
print(f"Dimension : {len(vector)}")
print(f"Premiers éléments : {vector[:5]}")