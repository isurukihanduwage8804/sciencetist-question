import streamlit as st
import os
import random
import time

st.set_page_config(page_title="විද්‍යා ප්‍රශ්න විචාරාත්මක වැඩසටහන", page_icon="🔬")

st.title("🔬 ලෝක ප්‍රකට පුද්ගලයින් හඳුනාගමු")

# ඔයා ලබා දුන් පිළිවෙලට අනුව දත්ත (කිසිම වෙනසක් කර නැත)
questions_list = [
    {"q_no": 1, "file": "1", "answer": "අයිසැක් නිව්ටන්"},
    {"q_no": 2, "file": "4", "answer": "ගැලීලියෝ ගැලිලි"},
    {"q_no": 3, "file": "7", "answer": "නීල් ආම්ස්ට්‍රෝන්"},
    {"q_no": 4, "file": "8", "answer": "යූරි ගගාරින්"},
    {"q_no": 5, "file": "9", "answer": "අර්නස්ට් රදර්ෆර්ඩ්"},
    {"q_no": 6, "file": "10", "answer": "හයිසන්බර්ග්"},
    {"q_no": 7, "file": "11", "answer": "ඇලෙක්සැන්ඩර් ග්‍රැහැම් බෙල්"},
    {"q_no": 8, "file": "12", "answer": "ජෝන් ලොගී බෙයාර්ඩ්"},
    {"q_no": 9, "file": "13", "answer": "මාරි කියුරි"},
    {"q_no": 10, "file": "14", "answer": "පියරේ කියුරි"},
    {"q_no": 11, "file": "15", "answer": "වෝල්ටා"},
    {"q_no": 12, "file": "17", "answer": "නිකොලා ටෙස්ලා"},
    {"q_no": 13, "file": "18", "answer": "ජොහැන්නස් කෙප්ලර්"},
    {"q_no": 14, "file": "19", "answer": "ගැලීලියෝ ගැලිලි"},
    {"q_no": 15, "file": "20", "answer": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්"}
]

# වැරදි පිළිතුරු සඳහා භාවිතා කරන නාමාවලිය
all_names = list(set([q["answer"] for q in questions_list]))

# Session state එක පවත්වා ගැනීම
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'options' not in st.session_state:
    st.session_state.options = []

if st.session_state.current_index < len(questions_list):
    current_q = questions_list[st.session_state.current_index]
    img_filename = current_q["file"]
    correct_answer = current_q["answer"]
    
    # පිළිතුරු 4ක් සෑදීම
    if not st.session_state.options:
        wrong_choices = random.sample([n for n in all_names if n != correct_answer], 3)
        options = wrong_choices + [correct_answer]
        random.shuffle(options)
        st.session_state.options = options

    st.write(f"### ප්‍රශ්නය {current_q['q_no']} / {len(questions_list)}")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if os.path.exists(img_filename):
            st.image(img_filename, use_container_width=True)
        else:
            st.error(f"පින්තූරය '{img_filename}' හමු නොවීය.")

    with col2:
        st.write("**මෙම පින්තූරයේ සිටින්නේ කවුද?**")
        
        # මෙතැනදී on_change භාවිතා කර පිළිතුරක් තේරූ සැනින් ක්‍රියාත්මක වන ලෙස සැකසුවා
        def check_answer():
            user_choice = st.session_state[f"q_{st.session_state.current_index}"]
            if user_choice == correct_answer:
                st.toast(f"නිවැරදියි! ✅ මේ {correct_answer}", icon='🎉')
                st.session_state.score += 1
            else:
                st.toast(f"වැරදියි! ❌ නිවැරදි පිළිතුර: {correct_answer}", icon='⚠️')
            
            # තත්පර 1.5ක් පමණ වෙලාවක් ලබා දී ඊළඟ එකට යන්න
            time.sleep(1.5)
            st.session_state.current_index += 1
            st.session_state.options = []

        st.radio(
            "පිළිතුර තෝරන්න:", 
            st.session_state.options, 
            key=f"q_{st.session_state.current_index}",
            on_change=check_answer
        )

    st.progress(st.session_state.current_index / len(questions_list))

else:
    st.balloons()
    st.header("වැඩසටහන අවසන්! 🎉")
    st.subheader(f"ඔබේ ලකුණු සංඛ්‍යාව: {st.session_state.score} / {len(questions_list)}")
    if st.button("නැවත ආරම්භ කරන්න"):
        st.session_state.score = 0
        st.session_state.current_index = 0
        st.session_state.options = []
        st.rerun()
