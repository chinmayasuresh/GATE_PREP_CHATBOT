import streamlit as st
import json
import os

st.title("📘 GATE MCQ Practice")

subject = st.selectbox("📂 Select a subject:", ["Operating Systems", "Data Structures","DBMS", "Computer Network","COA"])

# Map subject to file
file_map = {
    "Operating Systems": "mcqs/operating_systems.json",
    "Data Structures": "mcqs/data_structures.json",
    "DBMS": "mcqs/dbms.json",
    "Computer Network": "mcqs/computer_network.json",
    "COA": "mcqs/coa.json"
    
}

file_path = file_map[subject]

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    for q in questions:
        st.markdown(f"**Q{q['id']}. {q['question']}**")
        selected = st.radio("Choose an option:", list(q["options"].values()), key=q["id"])
        correct_answer = q["options"][q["answer"]]

        if st.button(f"Check Answer for Q{q['id']}", key=f"btn{q['id']}"):
            if selected == correct_answer:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! Correct answer: {correct_answer}")
            st.info(f"💡 Explanation: {q['explanation']}")
else:
    st.error("⚠️ Could not load MCQs. Check your file path.")





