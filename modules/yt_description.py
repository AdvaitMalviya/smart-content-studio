import streamlit as st
from utils.openai_utils import ask_gpt

def render():
    st.header("🎥 YouTube Title & Description Generator")

    content = st.text_area("Paste your video script or summary")

    if st.button("Generate Title & Description"):
        with st.spinner("Generating..."):
            title = ask_gpt(f"Create a catchy YouTube video title for this content:\n{content}")
            description = ask_gpt(f"Write an SEO-optimized YouTube description for this video:\n{content}")

            st.subheader("📌 Title")
            st.write(title)

            st.subheader("📝 Description")
            st.write(description)
