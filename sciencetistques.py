import streamlit as st
import os
import random

st.set_page_config(page_title="විද්‍යාඥයින් හඳුනාගමු", page_icon="🔬")

st.title("🔬 ලෝක ප්‍රකට පුද්ගලයින් කවුද?")
st.write("පින්තූරය බලා නිවැරදි පිළිතුර තෝරන්න.")

# පින්තූර සහ පිළිතුරු (මෙතන පිළිතුරු වලට සිංහල නම් භාවිතා කළ හැක)
data = {
    "1": "ඇල්බට් අයින්ස්ටයින්",
    "4": "තෝමස් එඩිසන්",
    "7": "මාරි කියුරි",
    "8": "අයිසැක් නිව්ටන්",
    "9": "නිකොලා ටෙස්ලා",
    "10": "චාල්ස් ඩාවින්",
    "11": "ඇලෙක්සැන්ඩර් ග්‍රැහැම් බෙල්",
    "12": "ගැලීලියෝ ගැලිලි",
    "13": "රයිට් සහෝදරයෝ",
    "14": "ลියනාඩෝ ඩා වින්චි",
    "15": "මයිකල් ෆැරඩේ",
    "17": "ස්ටීවන් හෝකින්",
    "18": "බෙන්ජමින් ෆ්‍රැන්ක්ලින්",
    "19": "ලුවී පාස්චර්",
    "20": "ස්ටීව් ජොබ්ස්"
}

# සියලුම නම් ලැයිස්තුවක් (වැරදි පිළිතුරු සෑදීමට)
all_names = list(data.values())

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'options' not in st.session_state:
    st.session_state.options = []

image_files = list(data.keys())

def next_question():
    st.session_state.current_index += 1
    st.session_state.options = [] # ඊළඟ ප්‍රශ්නයට පිළිතුරු අලුත් කරන්න

if st.session_state.current_index < len(image_files):
    img_filename = image_files[st.session_state.current_index]
    correct_answer = data[img_filename]
    
    # පිළිතුරු 4ක් සෑදීම (එක් වරක් පමණක්)
    if not st.session_state.options:
        wrong_answers = random.sample([n for n in all_names if n != correct_answer], 3)
        options = wrong_answers + [correct_answer]
        random.shuffle(options)
        st.session_state.options = options

    col1, col2 = st.columns([1, 1])
    
    with col1:
        if os.path.exists(img_filename):
            st.image(img_filename, use_container_width=True)
        else:
            st.error(f"පින්තූරය පේන්න නැහැ: '{img_filename}'")
    
    with col2:
        st.write(f"### ප්‍රශ්න අංකය: {st.session_state.current_index + 1} / {len(image_files)}")
        st.write("**මෙම පුද්ගලයා කවුද?**")
        
        # පිළිතුරු තෝරන්න (Radio buttons)
        choice = st.radio("නිවැරදි පිළිතුර තෝරන්න:", st.session_state.options, key=f"radio_{st.session_state.current_index}")
        
        if st.button("පිළිතුර තහවුරු කරන්න"):
            if choice == correct_answer:
                st.success(f"නිවැරදියි! මේ {correct_answer}")
                st.session_state.score += 1
            else:
                st.error(f"වැරදියි. නිවැරදි පිළිතුර: {correct_answer}")
            
            st.button("ඊළඟ පින්තූරය ➡️", on_click=next_question)

    st.progress(st.session_state.current_index / len(image_files))
