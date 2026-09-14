
import streamlit as st

from app.executor import question_to_sql


# --------------------------------------------------
# Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Progression — Sales Intelligence",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Interface
# --------------------------------------------------

st.title("📊 Progression — Sales Intelligence Assistant")

st.write(
    "Posez vos questions concernant vos données commerciales."
)


# --------------------------------------------------
# Historique de conversation
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Afficher l'historique
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        if "data" in message:
            st.dataframe(
                message["data"],
                use_container_width=True
            )


# --------------------------------------------------
# Nouvelle question
# --------------------------------------------------

question = st.chat_input(
    "Posez votre question..."
)


# --------------------------------------------------
# Traitement
# --------------------------------------------------

if question:

    # Ajouter la question à l'historique
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Afficher la question immédiatement
    with st.chat_message("user"):
        st.write(question)

    # Générer la réponse
    with st.chat_message("assistant"):

        with st.spinner("Analyse de votre question..."):

            try:

                result = question_to_sql(question)

                st.success("Requête exécutée avec succès.")

                if result:

                    st.dataframe(
                        result,
                        use_container_width=True
                    )

                    # Sauvegarder la réponse et les données
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Requête exécutée avec succès.",
                        "data": result
                    })

                else:

                    st.info("Aucun résultat trouvé.")

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Aucun résultat trouvé."
                    })

            except Exception as e:

                st.error("Une erreur est survenue.")

                st.exception(e)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"Erreur : {str(e)}"
                })
