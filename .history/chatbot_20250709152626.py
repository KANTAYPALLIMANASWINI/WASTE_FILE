from modules import resume_builder, missing_skills

def get_bot_response(user_input):
    user_input = user_input.lower()

    # 🌟 Warm & Friendly Greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "hii", "hlo,H"]):
        return (
            "Hey there! 👋😊 So glad to see you!\n"
            "I'm your AI Career Companion 💼✨\n"
            "Ask me anything about your resume, skills, or career path 💖"
        )

    # 📄 Resume-related help
    elif "resume" in user_input:
        return (
            "Sure! 📄 Please upload your resume below so I can analyze it and help you shine brighter ✨"
        )

    # 🧠 Skills & Missing Skills
    elif "skills" in user_input or "missing" in user_input:
        return (
            "I'll take a look at your current skills and suggest what you can learn next 🔍📘"
        )

    # 💼 Job Suggestions
    elif "job" in user_input or "career" in user_input:
        return (
            "Based on your resume, I’ll help suggest the best job role for you 💼💡"
        )

    # 💝 Thanks
    elif "thank" in user_input:
        return "Awww you're always welcome . I'm always here for you 💖"

    # 💬 Default fallback
    else:
        return (
            "I'm here to guide your career journey 🌈\n"
            "Upload your resume, ask about skills, or say hi anytime 🤖💬"
        )
