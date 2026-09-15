import streamlit as st
from pathlib import Path
import pandas as pd

from app.integration.main_pipeline import process_question


# ==================================================
# CONFIGURATION
# ==================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "image_sales.webp"

st.set_page_config(
    page_title="Sales Intelligence Assistant",
    page_icon=str(IMAGE_PATH),
    layout="wide"
)


# ==================================================
# INTERFACE
# ==================================================

col1, col2 = st.columns([0.8, 8])

with col1:
    st.markdown(
        "<div style='height: 5px;'></div>",
        unsafe_allow_html=True
    )

    st.image(
        str(IMAGE_PATH),
        width=300
    )

with col2:
    st.markdown(
        "<h1 style='margin-top: 0px;'>Sales Intelligence Assistant</h1>",
        unsafe_allow_html=True
    )

st.write(
    "Posez vos questions concernant vos données commerciales."
)


# ==================================================
# HISTORIQUE
# ==================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==================================================
# AFFICHAGE DES RESULTATS
# ==================================================

def display_result(result):

    if result is None:
        st.info("Aucun résultat trouvé.")
        return

    # ----------------------------------------------
    # DataFrame
    # ----------------------------------------------

    if isinstance(result, pd.DataFrame):

        if result.empty:
            st.info("Aucun résultat trouvé.")
            return

        result = result.copy()

        # ------------------------------------------
        # Traduction des colonnes
        # ------------------------------------------

        column_names = {
            "customer_id": "Client",
            "client_id": "Client",
            "product_id": "Produit",
            "order_id": "Commande",

            "chiffre_affaires": "Chiffre d'affaires",
            "ca": "Chiffre d'affaires",
            "revenue": "Chiffre d'affaires",
            "total_revenue": "Chiffre d'affaires",

            "marge": "Marge",
            "margin": "Marge",
            "total_margin": "Marge totale",

            "quantity": "Quantité",
            "quantite": "Quantité",

            "count": "Nombre",
            "order_count": "Nombre de commandes",

            "date": "Date",
            "month": "Mois",
            "year": "Année",

            "status": "Statut",

            "name": "Nom",
            "product_name": "Produit",
            "customer_name": "Client"
        }

        result.rename(
            columns={
                column: column_names.get(column, column)
                for column in result.columns
            },
            inplace=True
        )

        # ------------------------------------------
        # Détection des colonnes monétaires
        # ------------------------------------------

        currency_keywords = [
            "chiffre",
            "revenue",
            "revenu",
            "marge",
            "margin",
            "prix",
            "price",
            "montant",
            "amount"
        ]

        for column in result.columns:

            column_lower = str(column).lower()

            if any(
                keyword in column_lower
                for keyword in currency_keywords
            ):

                if pd.api.types.is_numeric_dtype(result[column]):

                    result[column] = result[column].apply(
                        lambda x:
                        f"{float(x):,.2f} €"
                        .replace(",", " ")
                        .replace(".", ",")
                        if pd.notna(x)
                        else ""
                    )

        # ------------------------------------------
        # Formatage des nombres entiers
        # ------------------------------------------

        for column in result.columns:

            if pd.api.types.is_integer_dtype(result[column]):

                result[column] = result[column].apply(
                    lambda x:
                    f"{x:,}".replace(",", " ")
                    if pd.notna(x)
                    else ""
                )

        # ------------------------------------------
        # Affichage
        # ------------------------------------------

        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )

        return

    # ----------------------------------------------
    # Résultat texte
    # ----------------------------------------------

    if isinstance(result, str):

        st.write(result)

        return

    # ----------------------------------------------
    # Autres résultats
    # ----------------------------------------------

    st.write(result)


# ==================================================
# AFFICHER L'HISTORIQUE
# ==================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        if "data" in message:
            display_result(message["data"])


# ==================================================
# CHAMP DE SAISIE
# ==================================================

question = st.chat_input(
    "Posez votre question..."
)


# ==================================================
# TRAITEMENT DE LA QUESTION
# ==================================================

if question:

    # ----------------------------------------------
    # Ajouter la question à l'historique
    # ----------------------------------------------

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # ----------------------------------------------
    # Afficher la question
    # ----------------------------------------------

    with st.chat_message("user"):
        st.write(question)

    # ----------------------------------------------
    # Générer la réponse
    # ----------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Analyse de votre question..."):

            try:

                result = process_question(question)

                display_result(result)

                # Ajouter le résultat à l'historique
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "Résultat de l'analyse :",
                    "data": result
                })

            except Exception as e:

                st.error(
                    "Une erreur est survenue lors du traitement de votre question."
                )

                st.exception(e)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"Erreur : {str(e)}"
                })