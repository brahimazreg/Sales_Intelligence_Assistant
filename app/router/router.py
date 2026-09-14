from app.llm import get_llm


def route_question(question):

    llm = get_llm()

    prompt = f"""
Tu es un routeur pour un assistant d'intelligence commerciale.

Tu dois classer la question utilisateur dans UNE SEULE catégorie :

SQL :
La réponse peut être obtenue uniquement à partir des données
présentes dans la base MySQL.

RAG :
La question demande uniquement une information métier,
une définition, une règle, une politique ou une explication
présente dans la documentation métier.

HYBRID :
La question nécessite à la fois :
- des informations métier provenant de la documentation RAG
- et des données provenant de MySQL.

Exemples :

Question : Quel est le chiffre d'affaires par client ?
Réponse : SQL

Question : Quel est le meilleur produit ?
Réponse : SQL

Question : Quelle est la définition du chiffre d'affaires ?
Réponse : RAG

Question : Quelle est la règle de calcul de la marge ?
Réponse : RAG

Question : Quelle est la marge totale en excluant les commandes annulées ?
Réponse : HYBRID

Question utilisateur :
{question}

Réponds uniquement avec :
SQL
ou
RAG
ou
HYBRID
"""

    response = llm.invoke(prompt)

    route = response.content.strip().upper()

    if route not in {"SQL", "RAG", "HYBRID"}:
        raise ValueError(
            f"Route invalide retournée par le LLM : {route}"
        )

    return route
# just for test
if __name__ == "__main__":

    questions = [
        "Quel est le chiffre d'affaires par client",
        "Quelle est la définition du chiffre d'affaires",
        "Quelle est la marge totale en excluant les commandes annulées",
    ]

    for question in questions:

        route = route_question(question)

        print("\nQuestion :", question)
        print("Route :", route)