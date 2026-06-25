import streamlit as st
from data_store import load_messages

st.title("📩 Boîte RH - Messages classés")

messages = load_messages()

if not messages:
    st.info("Aucun message reçu pour le moment.")
else:
    for item in messages:
        msg = item.get("text", "")
        label = item.get("category", "")

        st.write("📨 Message:", msg)
        st.write("🏷️ Catégorie:", label)
        st.divider()
