
from app.llm import get_llm


def route_question(question):

    llm = get_llm()

    prompt = f"""
Tu es un routeur pour un assistant d'intelligence commerciale.

Ta tâche est de classer la question utilisateur dans UNE SEULE catégorie.

CATÉGORIES AUTORISÉES :

SQL
La réponse peut être obtenue uniquement à partir des données
présentes dans la base MySQL.

RAG
La question demande uniquement une information métier,
une définition, une règle, une politique ou une explication
présente dans la documentation métier.

HYBRID
La question nécessite à la fois :
- une information métier provenant de la documentation RAG
- ET une valeur ou un calcul provenant des données MySQL.

EXEMPLES :

Question : Quel est le chiffre d'affaires par client ?
SQL

Question : Quel est le meilleur produit ?
SQL

Question : Quelle est la définition du chiffre d'affaires ?
RAG

Question : Quelle est la règle de calcul de la marge ?
RAG

Question : Quelle est la marge totale en excluant les commandes annulées ?
HYBRID

IMPORTANT :

Ta réponse doit contenir UNIQUEMENT UN des mots suivants :

SQL
RAG
HYBRID

N'ajoute aucune explication.
N'ajoute aucun commentaire.
N'ajoute aucune ponctuation.

QUESTION UTILISATEUR :
{question}

RÉPONSE :
"""

    response = llm.invoke(prompt)

    raw_route = response.content.strip().upper()

    print(f"Route brute retournée par le LLM : {raw_route}")

    # Sécurisation du résultat du LLM.
    # On cherche d'abord HYBRID car il contient aussi les termes
    # SQL et RAG dans certaines réponses explicatives.
    if "HYBRID" in raw_route:
        route = "HYBRID"
    elif "SQL" in raw_route:
        route = "SQL"
    elif "RAG" in raw_route:
        route = "RAG"
    else:
        raise ValueError(
            f"Route invalide retournée par le LLM : {raw_route}"
        )

    print(f"Route normalisée : {route}")

    return route


# Test
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
