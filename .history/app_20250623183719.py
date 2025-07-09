import streamlit as st
from login import login
from chatbot import get_bot_response
from modules import resume_builder

# Page setup
st.set_page_config(page_title="AI Career Companion", page_icon="🤖")
st.title("AI Career Companion 🤖💼")

# Login check
if login():
    st.success("You're logged in! Let's start your career journey 💖")

    # Chatbot section
    st.subheader("💬 Chat with Me")
    user_input = st.text_input("You:", "")

    if user_input:
        response = get_bot_response(user_input)
        st.text_area("Bot:", value=response, height=100)

    # Resume upload section
    st.subheader("📄 Upload Your Resume (PDF Only)")
    uploaded_file = st.file_uploader("Choose your resume file", type=["pdf"])

    if uploaded_file:
        with st.spinner("Analyzing your resume..."):
            result = resume_builder.build_resume(uploaded_file)
            st.success("Analysis complete! 💡")
            st.write(result)

else:
    st.warning("Please login from the sidebar to continue 🔐")
