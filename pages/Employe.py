import streamlit as st
from core.predict import predict
from data_store import save_message

st.title("📩 Espace Employé - Envoi de message")

text = st.text_area("Écrire un message client")

if st.button("Envoyer"):
    if text:
        category = predict(text)

        message = {
            "text": text,
            "category": category
        }

        save_message(message)

        st.success(f"Message envoyé ✔ Classé comme : {category}")
    else:
        st.warning("Écris un message")
