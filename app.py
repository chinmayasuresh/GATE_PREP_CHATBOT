import streamlit as st



st.set_page_config(page_title="GATE AI Assistant", layout="centered")

st.title("Welcome to GATE AI Assistant")
st.write("Choose a feature from the sidebar:")

st.markdown("### 📘 MCQs")
st.markdown("Practice GATE subject-wise multiple choice questions.")

st.markdown("### 🧠 Chatbot")
st.markdown("Ask theory questions like 'What is Normalization?' and get smart answers.")


# 👇 Sidebar Customization
with st.sidebar:
    st.markdown("## 🎓 GATE AI Assistant")
    
    st.markdown("### Features:")
    st.markdown("- **📘 MCQs**: Practice GATE subject-wise multiple choice questions.")
    st.markdown("- **🧠 Chatbot**: Get answers to your theoretical questions." )
    

    st.markdown("###  Made by Chinmaya")
