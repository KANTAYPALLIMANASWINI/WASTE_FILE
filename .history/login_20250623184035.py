import streamlit as st

# 🎯 Fixed username-passwords (you can change/add more)
USERS = {
    "manaswini": "1234",
    "admin": "admin"
}

def login():
    st.sidebar.title("🔐 Login Panel")
    username = st.sidebar.text_input("👤 Username")
    password = st.sidebar.text_input("🔑 Password", type="password")

    # 🌈 Login button
    if st.sidebar.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success(f"Welcome, {username}! 💖")
        else:
            st.error("❌ Invalid username or password")

    # ✅ Check session
    return st.session_state.get('logged_in', False)
