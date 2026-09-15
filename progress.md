# Progress - Sales Intelligence Assistant

## État du projet
Date : 2026-09-14

Le projet utilise :
- Python
- Streamlit
- MySQL
- ChromaDB pour le RAG
- Ollama / Qwen pour le LLM
- architecture SQL / RAG / HYBRID

---

## 1. Architecture actuelle

Le flux principal est :

Question utilisateur
        ↓
main_pipeline.py
        ↓
router.py
        ↓
SQL / RAG / HYBRID
        ↓
Résultat
        ↓
Streamlit

---

## 2. RAG

Le fichier `app/rag/retriever.py` contient :

- `embedding_question()`
- `retrieve_question(question, top_k)`

La fonction correcte est :

```python
retrieve_question


PROCHAINE ÉTAPE

Je me suis arrêté ici.

Objectif immédiat :

Améliorer l'affichage Streamlit

Actuellement :

Question :
Quelle est la marge totale en excluant les commandes annulées ?

Réponse :
Marge totale : 18900.47

Objectif :

La marge totale, hors commandes annulées, est de 18 900,47 €.

Mais les résultats tabulaires doivent continuer à être affichés comme des tableaux.

Il faut donc examiner le fichier Streamlit principal (app.py, streamlit_app.py ou autre) avant de modifier l'affichage.

Tests déjà validés
RAG

Question :

Quelle est la définition du chiffre d'affaires ?

→ RAG fonctionne.

HYBRID

Question :

Quelle est la marge totale en excluant les commandes annulées ?

→ HYBRID fonctionne.

Résultat :

18900.47000000
SQL

Question :

Quel est le chiffre d'affaires par client ?

→ doit être testé/validé dans le pipeline complet.

Fichiers principaux
app/
├── main_pipeline.py
├── router/
│   └── router.py
├── rag/
│   ├── retriever.py
│   └── embeddings.py
├── integration/
│   ├── sql_pipeline.py
│   ├── rag_pipeline.py
│   ├── hybrid_pipeline.py
│   └── generator_with_rag.py
├── connection.py
├── validator.py
├── schema.py
└── llm.py
Point de reprise

Quand on reprend le projet :

Vérifier le fichier Streamlit principal.
Améliorer l'affichage des résultats SQL/HYBRID.
Transformer les résultats simples en phrases naturelles.
Garder les DataFrames pour les requêtes nécessitant un tableau.
Harmoniser les règles métier RAG concernant les remises.
Tester les trois routes :
SQL
RAG
HYBRID
Tester ensuite l'application Streamlit de bout en bout.

Avec ce `progress.md`, si tu reviens plus tard et me dis simplement **« reprenons le projet depuis progress.md »**, j'aurai le contexte nécessaire pour reprendre directement au niveau de **l'affichage Streamlit**, sans refaire tout le debugging précédent.