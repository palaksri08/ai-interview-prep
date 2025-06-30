import streamlit as st
from prompts import generate_questions_prompt, feedback_prompt
from utils import extract_text_from_docx
import random

st.set_page_config(page_title="AI Interview Prep Assistant", page_icon="🧠")
st.title("🧠 AI Interview Prep Assistant (Demo Mode)")
st.markdown("This is a demo version of the app using mock interview content and mock feedback for display purposes.")

# Upload resume
resume_file = st.file_uploader("Upload your resume (.docx)", type=["docx"])

# Input for job role
job_role = st.text_input("Target Job Role (e.g., Data Scientist, Backend Developer):")

if resume_file and job_role:
    resume_text = extract_text_from_docx(resume_file)

    if st.button("Generate Interview Questions"):
        with st.spinner("Generating mock questions..."):
            # Mock questions based on job role
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
                    # Dynamic mock feedback
                    feedback_options = [
                        "Good answer! Consider adding a specific project as an example.",
                        "Nice! You can enhance your response by showing impact or metrics.",
                        "That's a start! Try relating it to real-world tools or technologies.",
                        "You’ve touched the surface. Expand on your role or thought process.",
                        "Decent response. It’ll be stronger with a STAR method approach."
                    ]
                    feedback = random.choice(feedback_options)
                    st.info(f"💬 Feedback: {feedback}")

