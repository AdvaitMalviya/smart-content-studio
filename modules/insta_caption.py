import streamlit as st
from utils.openai_utils import ask_gpt

def render():
    st.header("📸 Instagram Caption Assistant")

    post_desc = st.text_area("Describe your post", "Sunset by the beach")

    if st.button("Generate Caption"):
        with st.spinner("Generating..."):
            prompt = f"Create an engaging Instagram caption with emojis and hashtags for: {post_desc}"
            caption = ask_gpt(prompt)
            st.success("Caption:")
            st.write(caption)
