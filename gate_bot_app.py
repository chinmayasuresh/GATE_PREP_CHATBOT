import streamlit as st
import json
import os
from langchain_ollama import OllamaLLM

# Load Ollama model once
llm = OllamaLLM(model="llama3")
st.markdown("""
    <style>
    body {
        background-color: #f9f9f9;
    }
    .stRadio > label {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="GATE Prep Chatbot", layout="centered")

st.markdown("<h1 style='text-align: center;'>📚 GATE Prep AI Agent</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🧠 Select Preferences")
    subject = st.selectbox("📘 Subject", ["Operating Systems", "Data Structures", "DBMS"])
    mode = st.radio("🎯 Choose Mode", ["📝 MCQ Practice", "💬 Ask a Doubt"])

# Filename mapping
subject_map = {
    "Operating Systems": "operating_systems.json",
    "Data Structures": "data_structures.json",
    "DBMS": "dbms.json"
}

filename = f"mcqs/{subject_map[subject]}"

# MCQ Mode
if mode == "📝 MCQ Practice":
    st.subheader(f"📝 Practice Questions: {subject}")
    try:
        with open(filename, "r", encoding="utf-8-sig") as f:
            questions = json.load(f)

        for q in questions:
            st.markdown(f"**Q{q['id']}. {q['question']}**")
            user_answer = st.radio("Choose an option:", list(q["options"].values()), key=q['id'])

            correct_option_key = q["answer"]
            correct_option_text = q["options"][correct_option_key]

            if st.button(f"Check Answer #{q['id']}"):
                if user_answer == correct_option_text:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Incorrect. Correct Answer: **{correct_option_text}**")
                st.info(f"🧾 Explanation: {q['explanation']}")
            st.divider()

    except Exception as e:
        st.error(f"⚠️ Could not load MCQs: {str(e)}")

# Doubt Mode
elif mode == "💬 Ask a Doubt":
    st.subheader(f"💬 Ask Doubts in {subject}")
    question = st.text_input("🧠 Enter your GATE doubt (e.g., What is normalization?)")

    if st.button("Ask"):
        with st.spinner("🤔 Thinking..."):
            try:
                answer = llm.invoke(question)
                st.success("🧾 Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
