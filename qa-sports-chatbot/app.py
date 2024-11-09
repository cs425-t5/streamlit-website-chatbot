import streamlit as st
import utils
import utils_model2
import utils_model3

# Streamlit UI
st.subheader("Sports QA Chatbot 💬", divider="rainbow")
st.caption(
    """Chatbot using :rainbow[cross attention and self-attention]"""
)

# Who is the best basketball player?
if user_query := st.text_input(
    key="one",
    label="Ask a question about Rugby 🏉, Soccer ⚽ or Basketball 🏀!",
    placeholder="How many field goals did Kobe Bryant score?",
):
    # Get the answers
    with st.spinner("Waiting"):
        answer = utils.generate_ans(user_query)
        st.divider()

st.caption(
    """Chatbot using :rainbow[multiplicative attention]"""
)
# Who is the best basketball player?
if user_query := st.text_input(
    label="Ask a question about Rugby 🏉, Soccer ⚽ or Basketball 🏀!",
    placeholder="How many field goals did Kobe Bryant score?",
):
    # Get the answers
    with st.spinner("Waiting"):
        answer = utils_model2.generate_ans(user_query)
        st.divider()

st.caption(
    """Chatbot using :rainbow[multiplicative attention] with 512 dim"""
)
# Who is the best basketball player?
if user_query := st.text_input(
    key="three",
    label="Ask a question about Rugby 🏉, Soccer ⚽ or Basketball 🏀!",
    placeholder="How many field goals did Kobe Bryant score?",
):
    # Get the answers
    with st.spinner("Waiting"):
        answer = utils_model3.generate_ans(user_query)
        st.divider()