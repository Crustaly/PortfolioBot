import openai
import streamlit as st
from PIL import Image
from streamlit.components.v1 import html


col1, mid, col2 = st.columns([1, 4, 20])
with col1:
    st.image("logo.png", width=150)
with col2:
    st.write("")
    st.write("")

    st.title("         " + "      PortfolioBot")
st.header("Creating an professional portfolio with NLP")
st.write("Created by Crystal Yang")
st.subheader("Natural Language Processesing is made possible by ChatGPT API")
st.image("chat.jpg", width=150)
st.subheader(
    "This application was created with Streamlit, which is a python based web development software"
)
st.image("stm.jpg", width=150)
