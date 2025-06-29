# 🎓 GATE AI Prep Chatbot

An AI-powered web app that helps you prepare for the GATE exam with:
- 📘 Subject-wise Multiple Choice Questions (MCQs)
- 🤖 A smart chatbot that answers theoretical questions
- 🔊 Voice-based responses
- 💻 Simple, friendly user interface

---

## 🌟 Features

- ✅ **Subject-wise MCQs**: Practice Operating Systems, DSA, DBMS, etc.
- 🧠 **AI Chatbot**: Ask open-ended questions like “What is normalization?”
- 💬 **Instant Feedback**: See whether your answer is correct with explanations
- 🔊 **Text-to-Speech**: Bot reads answers out loud using voice
- 🚪 **No Sign-In Required**: Just open and start learning
- 🎨 **User-Friendly Interface**: Streamlit-powered UI with clean navigation

---

## 📁 Folder Structure

gate_chatbot/
├── app.py # Home page
├── pages/
│ ├── 1_📘_MCQs.py # MCQ page
│ └── 2_🧠_Chatbot.py # Chatbot page
├── mcqs/
│ ├── operating_systems.json
│ └── data_structures.json
      ......
├── requirements.txt
└── README.md

---

## 🚀 How to Run It Locally

### 1. ✅ Install Python dependencies:
```bash
pip install -r requirements.txt
🧠 Start Ollama with LLaMA 3:
ollama run llama3
🎯 Run the Streamlit app:
streamlit run app.py
