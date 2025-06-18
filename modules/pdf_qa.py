import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.openai_utils import ask_gpt

def render():
    st.header("📚 Chat with Notes (PDF Q&A)")

    uploaded_file = st.file_uploader("Upload your notes (PDF)", type="pdf")
    question = st.text_input("Ask a question about your notes")

    if uploaded_file and question:
        with st.spinner("Reading and answering..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
            prompt = f"Based on these notes:\n{pdf_text}\n\nAnswer the question: {question}"
            answer = ask_gpt(prompt)
            st.success("Answer:")
            st.write(answer)
