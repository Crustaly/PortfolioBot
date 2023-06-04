
import openai
import streamlit as st
from PIL import Image
from streamlit.components.v1 import html






button_style = """
        <style>
        .stButton > button {
    width:300px;
    height:100px;

        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)



col1, mid, col2 = st.columns([1,4,20])
with col1:
    st.image('logo.png', width=150)
with col2:
    st.write("")
    st.write("")
 
    st.title("         " +"      PortfolioBot")

st.header('Creating an professional portfolio with NLP')
st.write('Created by Crystal Yang')
simple = "Just write down the things you're proud of using simple words, and we will generate a customized and professional portfolio for you!"
st.subheader(simple)
st.title("")
st.title("")
st.title("")



col1, col2 = st.columns([1.2,1])
with col1:
    st.button("Get Started!")
with col2:
    st.button("How this works")


