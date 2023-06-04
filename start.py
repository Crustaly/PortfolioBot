import streamlit as st
import time
from PIL import Image


st.title("Make your portfolio here!")
st.header("Just follow our simple steps, and you're done!")
st.write(" ")
st.subheader("1. Write your experiences here, in super simple words")
st.write("(We will make it sound fancy and professional)")
st.caption(
    'For example, if you write "I volunteered to take care of three dogs at a shelter", we will write "Passionately volunteered at a renowned shelter, nurturing and tending to three beloved canines selflessly."'
)
st.caption("Enter each achievement on a new line.")
txt = st.text_area


text = st.text_area("Enter Text Below (maximum 500 words):", height=300)

st.subheader("2. Enter your skills")
st.caption("Seperate each skill with a comma.")
text = st.text_area("Enter Text Below (maximum 200 words):", height=100)
st.title(" ")
st.subheader("3. Upload a high quality headshot")
st.write("This will be used on your portfolio, so make sure it is professional!")
st.caption("Upload a PNG or a JPG")

fi = st.file_uploader("Please choose a file")
st.title(" ")
st.subheader("4. Enter your contact information")
st.write("This will be displayed on your portfolio")
text = st.text_input("Enter your first and last name:")
text = st.text_input("Enter a valid email:")
text = st.text_input("Enter a valid phone number:")
# idk if theres other things you need on a portfolio
# give option for portfolio types

st.subheader("5. Pick a resume template")
st.write("We will put your information here!")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.subheader("Simple:")
    st.image("basic.png", width=220)


with col2:
    st.subheader("Eye-catching:")
    st.image("eye-catching.png", width=220)
with col3:
    st.subheader("Elegant:")
    st.image("ele.png", width=220)

option = st.selectbox(
    "Which template do you prefer?", ("Simple", "Eye-catching", "Elegant")
)

st.title("")

submit = st.button("Generate")

if submit:
    with st.spinner("Generating your elegant portfolio..."):
        time.sleep(5)
    st.success("Done!")
    with open("pdf.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Click here to download your resume!",
        data=PDFbyte,
        file_name="res.pdf",
        mime="application/octet-stream",
    )
