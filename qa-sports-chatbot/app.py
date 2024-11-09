import streamlit as st
import utils
import utils_model2
import utils_model3

# Streamlit UI
st.subheader("Sports QA Chatbot 💬", divider="rainbow")
st.caption(
    """Chatbot using :rainbow[cross attention and self-attention]"""
)

# Model input
if user_query1 := st.text_input(
    key="one",
    label="Ask a question about Rugby 🏉, Soccer ⚽ or Basketball 🏀!",
    placeholder="How many field goals did Kobe Bryant score?"
):
    with st.spinner("Waiting"):
        answer = utils.generate_ans(user_query1)
        st.divider()

st.caption(
    """Chatbot using :rainbow[multiplicative attention]"""
)

if user_query2 := st.text_input(
    key="two",
    label="Ask a question about Rugby 🏉, Soccer ⚽ or Basketball 🏀!",
    placeholder="How many field goals did Kobe Bryant score?"
):
    with st.spinner("Waiting"):
        answer = utils_model2.generate_ans(user_query2)
        st.divider()

st.caption(
    """Chatbot using :rainbow[multiplicative attention] with 512 dim"""
)

if user_query3 := st.text_input(
    key="three",
    label="Ask a question about Rugby 🏉, Soccer ⚽ or Basketball 🏀!",
    placeholder="How many field goals did Kobe Bryant score?"
):
    with st.spinner("Waiting"):
        answer = utils_model3.generate_ans(user_query3)
        st.divider()
