import streamlit as st
import utils

# Streamlit UI
st.subheader("🔎 Sports QA bot", divider="rainbow")
st.caption(
    """This website hosts a chatbot built using a Transformers architecture. It has been trained to answer questions related to rugby, soccer and basketball matches and players."""
)

# Who is the best basketball player?
if user_query := st.text_input(
    label="Ask a question about Rugby 🏉, Soccer ⚽ or Basketball 🏀!",
    placeholder="How many field goals did Kobe Bryant score?",
):
    # Get the answers
    with st.spinner("Waiting"):
        answer = utils.generate_ans(user_query)
        st.divider()
