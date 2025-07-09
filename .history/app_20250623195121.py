import streamlit as st
from login import login
from chatbot import get_bot_response
from modules import resume_builder, missing_skills

# Page setup
st.set_page_config(page_title="AI Career Companion", page_icon="🤖")
st.title("AI Career Companion 🤖💼")

# Login check
if login():
    st.success("You're logged in! Let's start your career journey 💖")

    # 💬 Chatbot section
    st.subheader("💬 Chat with Me")
    user_input = st.text_input("You:", "")

    if user_input:
        response = get_bot_response(user_input)
        st.text_area("Bot:", value=response, height=100)

    # 📄 Resume upload section
    st.subheader("📄 Upload Your Resume (PDF Only)")
    uploaded_file = st.file_uploader("Choose your resume file", type=["pdf"])

    if uploaded_file:
        with st.spinner("Analyzing your resume..."):
            result = resume_builder.build_resume(uploaded_file)
            st.success("Analysis complete! 💡")

            # ✅ Show extracted result
            st.subheader("📊 Resume Summary:")
            st.write(f"✅ **Extracted Skills:** {', '.join(result['Extracted Skills'])}")
            st.write(f"🎯 **Predicted Job Role:** {result['Predicted Job Role']}")
            st.write(f"⭐ **Resume Rating (Out of 10):** {result['Resume Rating (out of 10)']}")

            # ✅ Get missing skills
            missing = missing_skills.find_missing_skills(
                result["Extracted Skills"], result["Predicted Job Role"]
            )
            links = missing_skills.get_learning_links(missing)

            st.subheader("❌ Missing Skills for Your Target Role:")
            if missing:
                for skill in missing:
                    st.write(f"- {skill}")
            else:
                st.success("🎉 You have all the required skills!")

            # ✅ Learning links
            st.subheader("🎓 Suggested Learning Resources:")
            if links:
                for skill, link in links.items():
                    st.markdown(f"🔗 **{skill.title()}**: [Click to Learn]({link})")
            else:
                st.info("No learning resources to suggest!")

else:
    st.warning("Please login from the sidebar to continue 🔐")
