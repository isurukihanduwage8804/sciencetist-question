import streamlit as st
import random

# 1. විද්‍යාඥයින්ගේ දත්ත (පින්තූර ලින්ක් සහ පිළිතුරු)
SCIENTISTS = [
    {
        "name": "Albert Einstein",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
        "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Marie Curie"]
    },
    {
        "name": "Marie Curie",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Marie_Curie_2.jpg",
        "options": ["Charles Darwin", "Marie Curie", "Ada Lovelace", "Rosalind Franklin"]
    },
    {
        "name": "Isaac Newton",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/39/GodfreyKneller-IsaacNewton-1689.jpg",
        "options": ["Galileo Galilei", "Isaac Newton", "Thomas Edison", "Louis Pasteur"]
    },
    {
        "name": "Nikola Tesla",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/79/Tesla_circa_1890.jpg",
        "options": ["Guglielmo Marconi", "Nikola Tesla", "Alexander Graham Bell", "Michael Faraday"]
    }
]

st.title("🔬 Science Heroes: Quiz Time!")
st.subheader("පින්තූරයේ සිටින විද්‍යාඥයා කවුදැයි හඳුනාගන්න.")

# Session State මගින් ප්‍රශ්න තෝරාගැනීම
if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(SCIENTISTS)
    st.session_state.feedback = ""

q = st.session_state.current_q

# පින්තූරය පෙන්වීම (Auto load from URL)
col1, col2 = st.columns([1, 1])

with col1:
    st.image(q["image"], width=300, caption="කවුද මේ?")

with col2:
    # බහුවරණ පිළිතුරු 4 පෙන්වීම
    user_choice = st.radio("නිවැරදි පිළිතුර තෝරන්න:", q["options"])
    
    if st.button("Submit Answer"):
        if user_choice == q["name"]:
            st.session_state.feedback = "✅ නිවැරදියි! ඉතා හොඳයි."
        else:
            st.session_state.feedback = f"❌ වැරදියි. මොහු {q['name']} යි."

# ප්‍රතිඵලය පෙන්වීම
if st.session_state.feedback:
    st.info(st.session_state.feedback)
    if st.button("Next Question ➡️"):
        st.session_state.current_q = random.choice(SCIENTISTS)
        st.session_state.feedback = ""
        st.rerun()

st.divider()
st.caption("මෙම පින්තූර අන්තර්ජාලයෙන් ස්වයංක්‍රීයව (Auto-set) ලබාගන්නා ඒවා වේ.")
