import streamlit as st
import os
import random

st.set_page_config(page_title="විද්‍යා ප්‍රශ්න විචාරාත්මක වැඩසටහන", page_icon="🔬")

st.title("🔬 ලෝක ප්‍රකට පුද්ගලයින් හඳුනාගමු")
st.write("ප්‍රශ්න පිළිවෙලට අනුව නිවැරදි පිළිතුර තෝරන්න.")

# ඔයා ලබා දුන් පිළිවෙලට අනුව පිළිතුරු ලැයිස්තුව (පිළිවෙල 1, 2, 3...)
# පින්තූර ෆයිල් එකේ නම සහ පිළිතුර මෙහි ගලපා ඇත
questions_data = [
    {"file": "1", "answer": "අයිසැක් නිව්ටන්"},
    {"file": "4", "answer": "ගැලීලියෝ ගැලිලි"}, # ඔයාගේ පිළිවෙලට 2 වැනි ප්‍රශ්නය
    {"file": "7", "answer": "නීල් ආම්ස්ට්‍රෝන්"}, # 3 වැනි ප්‍රශ්නය
    {"file": "8", "answer": "යූරි ගගාරින්"},     # 4 වැනි ප්‍රශ්නය
    {"file": "9", "answer": "අර්නස්ට් රදර්ෆර්ඩ්"}, # 5 වැනි ප්‍රශ්නය
    {"file": "10", "answer": "හයිසන්බර්ග්"},      # 6 වැනි ප්‍රශ්නය
    {"file": "11", "answer": "ජෝන් ලොගී බෙයාර්ඩ්"}, # 8 වැනි ප්‍රශ්නය (ඔයාගේ අංකනයට අනුව)
    {"file": "12", "answer": "මාරි කියුරි"},      # 9 වැනි ප්‍රශ්නය
    {"file": "13", "answer": "පියරේ කියුරි"},      # 10 වැනි ප්‍රශ්නය
    {"file": "14", "answer": "නිකොලා ටෙස්ලා"},     # 12 වැනි ප්‍රශ්නය
    {"file": "15", "answer": "ජොහැන්නස් කෙප්ලර්"}, # 13 වැනි ප්‍රශ්නය
    {"file": "17", "answer": "ගැලීලියෝ ගැලිලි"},    # 14 වැනි ප්‍රශ්නය
    {"file": "18", "answer": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්"}, # 15 වැනි ප්‍රශ්නය
    # ඉතිරි පින්තූර සඳහා (ප්‍රශ්න 20 සම්පූර්ණ කිරීමට)
    {"file": "19", "answer": "ලුවී පාස්චර්"},
    {"file": "20", "answer": "ස්ටීව් ජොබ්ස්"}
]

# වැරදි පිළිතුරු සෑදීමට සියලුම නම් එකතු කර ගැනීම
all_possible_names = list(set([item["answer"] for item in questions_data]))

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'options' not in st.session_state:
    st.session_state.options = []
if 'answered' not in st.session_state:
    st.session_state.answered = False

def next_question():
    st.session_state.current_index += 1
    st.session_state.options = []
    st.session_state.answered = False

if st.session_state.current_index < len(questions_data):
    current_q = questions_data[st.session_state.current_index]
    img_filename = current_q["file"]
    correct_answer = current_q["answer"]
    
    # පිළිතුරු 4ක් සෑදීම
    if not st.session_state.options:
        wrong_answers = random.sample([n for n in all_possible_names if n != correct_answer], 3)
        options = wrong_answers + [correct_answer]
        random.shuffle(options)
        st.session_state.options = options

    col1, col2 = st.columns([1, 1])
    with col1:
        # GitHub root එකේ පින්තූරය ඇත්දැයි බැලීම
        if os.path.exists(img_filename):
            st.image(img_filename, use_container_width=True)
        else:
            st.error(f"පින්තූරය '{img_filename}' හමු නොවීය.")

    with col2:
        st.write(f"### ප්‍රශ්නය {st.session_state.current_index + 1} / {len(questions_data)}")
        st.write("**මෙම පින්තූරයේ සිටින්නේ කවුද?**")
        
        choice = st.radio("නිවැරදි පිළිතුර තෝරන්න:", st.session_state.options, key=f"q_{st.session_state.current_index}")
        
        if not st.session_state.answered:
            if st.button("පිළිතුර තහවුරු කරන්න"):
                st.session_state.answered = True
                if choice == correct_answer:
                    st.success(f"නිවැරදියි! ✅")
                    st.session_state.score += 1
                else:
                    st.error(f"වැරදියි! ❌ නිවැරදි පිළිතුර: {correct_answer}")
                st.rerun()
        else:
            if st.button("ඊළඟ ප්‍රශ්නය ➡️"):
                next_question()
                st.rerun()
