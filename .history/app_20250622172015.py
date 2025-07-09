import streamlit as st

st.set_page_config(page_title="AI Career Chatbot", layout="centered")

st.title("💬 AI Career Companion Chatbot")
st.markdown("Hello! I'm your AI Buddy 🤖. Ask me anything about your resume, jobs, or skills!")

def get_reply(user_input):
    user_input = user_input.lower()

    if "resume" in user_input:
        from modules.module1_resume import parse_resume
        return parse_resume("resume.pdf")

    elif "predict job" in user_input or "which job":
        from modules.module2_predictor import predict_job
        return predict_job(['html', 'css', 'python', 'communication'])

    elif "rating" in user_input:
        from modules.module3_rating import rate_resume
        return rate_resume(['html', 'css', 'python', 'communication'])

    elif "match" in user_input:
        from modules.module4_matcher import get_matches
        return get_matches(['html', 'css', 'python', 'communication'])

    elif "missing skill" in user_input or "gap":
        from modules.module5_skills import find_missing_skills
        return find_missing_skills('Backend Developer', ['html', 'css', 'python', 'communication'])

    else:
        return "Sorry friend 😅 I don’t know that yet. Ask about your resume, jobs or skills!"

user_input = st.text_input("Type your question here 👇")
if st.button("Ask"):
    if user_input:
        reply = get_reply(user_input)
        st.success(reply)
    else:
        st.warning("Type something friend 💬")

st.caption("Made with 💖 by Manaswini  with her passion")
