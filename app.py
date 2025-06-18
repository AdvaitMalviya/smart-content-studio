import streamlit as st
from modules import (
    story_generator,
    resume_writer,
    pdf_qa,
    yt_description,
    image_caption,
    insta_caption
)

st.set_page_config(page_title="Smart Content Studio", layout="wide")
st.title("🤖 Smart Content Studio")

option = st.sidebar.selectbox("Select a Module", (
    "Story Generator",
    "Resume & Cover Letter",
    "Chat with Notes (PDF Q&A)",
    "YouTube Title & Description",
    "Image Captioning",
    "Instagram Caption Assistant"
))

if option == "Story Generator":
    story_generator.render()
elif option == "Resume & Cover Letter":
    resume_writer.render()
elif option == "Chat with Notes (PDF Q&A)":
    pdf_qa.render()
elif option == "YouTube Title & Description":
    yt_description.render()
elif option == "Image Captioning":
    image_caption.render()
elif option == "Instagram Caption Assistant":
    insta_caption.render()
