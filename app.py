import streamlit as st
from prompts import generate_questions_prompt, feedback_prompt
from utils import extract_text_from_docx

st.set_page_config(page_title="AI Interview Prep Assistant", page_icon="🧠")
st.title("🧠 AI Interview Prep Assistant (Demo Mode)")
st.markdown("This is a demo version of the app using mock interview content for display purposes.")

resume_file = st.file_uploader("Upload your resume (.docx)", type=["docx"])
job_role = st.text_input("Target Job Role (e.g., Data Scientist, Backend Developer):")

if resume_file and job_role:
    resume_text = extract_text_from_docx(resume_file)

    if st.button("Generate Interview Questions"):
        with st.spinner("Generating mock questions..."):
            # Mock interview questions
            mock_questions = [
                f"What challenges have you faced in {job_role} projects?",
                f"Explain a technical concept you used in a recent project.",
                f"How do you stay updated with {job_role} trends?",
                f"What’s your experience with collaboration in teams?",
                f"Why do you want to work as a {job_role}?"
            ]

            st.subheader("📋 Mock Interview Questions")

            for idx, question in enumerate(mock_questions):
                st.markdown(f"**Q{idx+1}:** {question}")
                user_answer = st.text_area(f"Your Answer to Q{idx+1}:")

                if user_answer:
                    st.success("💬 Mock Feedback: Good answer! You demonstrated understanding. Consider adding more depth or examples.")
