import streamlit as st
from utils.openai_utils import ask_gpt

def render():
    st.header("📖 AI Story Generator")
    prompt = st.text_area("Enter a story prompt", "A time traveler visits ancient Egypt")

    if st.button("Generate Story"):
        with st.spinner("Generating..."):
            response = ask_gpt(
                f"Write a short and creative story based on this prompt: {prompt}"
            )
            st.success("Here's your story:")
            st.write(response)
