import streamlit as st

# Redirect if not logged in
if not st.session_state.get("logged_in"):
    st.warning("🔐 Please login first.")
    st.stop()

st.title("🤖 GATE AI Chatbot")
st.write(f"Welcome back, {st.session_state['username']}!")

# Your chatbot UI here...
