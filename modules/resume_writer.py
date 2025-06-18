import streamlit as st
from utils.openai_utils import ask_gpt

def render():
    st.header("📄 Resume & Cover Letter Generator")

    name = st.text_input("Name")
    education = st.text_area("Education")
    experience = st.text_area("Work Experience")
    job_role = st.text_input("Target Job Role")

    if st.button("Generate Resume & Cover Letter"):
        with st.spinner("Generating..."):
            resume = ask_gpt(
                f"Create a professional resume for {name} with education: {education}, "
                f"experience: {experience}, targeting the role of {job_role}."
            )
            cover_letter = ask_gpt(
                f"Write a personalized cover letter for {name} applying for a {job_role} position "
                f"based on the above background."
            )

            st.subheader("📄 Resume")
            st.write(resume)

            st.subheader("✉️ Cover Letter")
            st.write(cover_letter)
