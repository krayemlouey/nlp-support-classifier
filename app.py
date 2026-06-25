import streamlit as st
from core.predict import predict
from data_store import save_message

st.title("Support Client - IA")

msg = st.text_area("Votre message")

if st.button("Envoyer"):
    result = predict(msg)
    st.success(f"Catégorie détectée : {result}")

    # sauvegarde pour RH
    save_message({
        "text": msg,
        "category": result
    })