
import streamlit as st
import requests

st.set_page_config(page_title="ChatBot Paludisme", layout="centered")
st.title("💬 ChatBot Paludisme")
st.markdown("Posez vos questions sur le paludisme et obtenez des réponses fiables à partir des données de l’OMS.")

theme = st.selectbox("Choisissez un thème", ["Prévention", "Symptômes", "Traitement", "Femmes enceintes", "Enfants", "Autre"])
question = st.text_input("❓ Posez votre question ici :")

if st.button("Envoyer"):
    if question.strip() != "":
        with st.spinner("⏳ Le chatbot réfléchit..."):
            query = f"{theme} : {question}"
            try:
                response = requests.post("http://localhost:8000/ask", json={"query": query})
                if response.status_code == 200:
                    st.success(response.json()["response"])
                else:
                    st.error("Erreur : Impossible de récupérer la réponse.")
            except Exception as e:
                st.error(f"Erreur de connexion : {e}")
    else:
        st.warning("Veuillez poser une question.")
