import streamlit as st
import ollama
import pyttsx3
import random

# ---------- Page Config ----------
st.set_page_config(page_title="GATE Chatbot", layout="centered")
st.title("🧠 GATE AI Chatbot")
st.write("Ask me anything from GATE topics like OS, DBMS, DSA, CN... I'm here to help! 💬")

# ---------- Encouragement ----------
encouragements = [
    "You're doing amazing, future GATE topper! 🚀",
    "Let’s crack this together! 💪",
    "Keep those doubts coming. I'm with you 😊",
    "One concept at a time — you're on the right track! 🌱",
    "Don’t worry, I’ll explain it clearly 💡"
]

st.info(random.choice(encouragements))

# ---------- Question Input ----------
query = st.text_input("💬 Your Question:")

# ---------- Only Run When User Enters a Question ----------
if query:
    with st.spinner("Thinking and explaining like a good teacher... 🎓"):

        # 🌟 Friendly personality via system prompt
        system_prompt = {
            "role": "system",
            "content": (
                "You are a friendly and supportive GATE preparation assistant. "
                "You explain concepts clearly, step by step, using easy words and examples. "
                "Be kind, patient, and sound like a helpful friend or teacher."
            )
        }

        # 🔗 Ask the model
        response = ollama.chat(
            model="llama3",
            messages=[
                system_prompt,
                {"role": "user", "content": query}
            ]
        )

        answer = response['message']['content']

        # ✅ Display Answer
        st.success("🧠 Here's your answer:")
        st.write(answer)

        # 🔊 Speak the answer
        engine = pyttsx3.init()
        engine.say(answer)
        engine.runAndWait()
