import streamlit as st
import os
import random

st.set_page_config(page_title="විද්‍යා ප්‍රශ්න විචාරාත්මක වැඩසටහන", page_icon="🔬")

st.title("🔬 ලෝක ප්‍රකට පුද්ගලයින් හඳුනාගමු")
st.write("පින්තූරය බලා නිවැරදි පිළිතුර තෝරන්න.")

# ඔයා ලබාදුන් නිවැරදි දත්ත ලැයිස්තුව
data = {
    "1": "අයිසැක් නිව්ටන්",
    "4": "යූරි ගගාරින්",
    "7": "මාරි කියුරි",
    "8": "ජෝන් ලොගී බෙයාර්ඩ්",
    "9": "මාරි කියුරි",
    "10": "පියරේ කියුරි",
    "11": "ඇලෙක්සැන්ඩර් ග්‍රැහැම් බෙල්",
    "12": "නිකොලා ටෙස්ලා",
    "13": "ජොහැන්නස් කෙප්ලර්",
    "14": "ගැලීලියෝ ගැලිලි",
    "15": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්",
    "17": "ස්ටීවන් හෝකින්",
    "18": "බෙන්ජමින් ෆ්‍රැන්ක්ලින්",
    "19": "ලුවී පාස්චර්",
    "20": "ස්ටීව් ජොබ්ස්"
}

# 2, 3, 5, 6 වැනි අංක සඳහා ඔයා ලබාදුන් නම් (ෆයිල් වලට ගැලපෙන ලෙස)
# සටහන: ඔයා එවපු අංක වලට අනුව මේවා එකතු කළා
extra_data = {
    "2": "ගැලීලියෝ ගැලිලි",
    "3": "නීල් ආම්ස්ට්‍රෝන්",
    "5": "අර්නස්ට් රදර්ෆර්ඩ්",
    "6": "හයිසන්බර්ග්"
}
data.update(extra_data)

# සියලුම නම් ලැයිස්තුවක් (වැරදි පිළිතුරු සෑදීමට)
all_names = list(set(data.values()))

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'options' not in st.session_state:
    st.session_state.options = []
if 'answered' not in st.session_state:
    st.session_state.answered = False

image_files = sorted(list(data.keys()), key=lambda x: int(x))

def next_question():
    st.session_state.current_index += 1
    st.session_state.options = []
    st.session_state.answered = False

if st.session_state.current_index < len(image_files):
    img_filename = image_files[st.session_state.current_index]
    correct_answer = data[img_filename]
    
    # පිළිතුරු 4ක් සෑදීම
    if not st.session_state.options:
        other_names = [n for n in all_names if n != correct_answer]
        wrong_answers = random.sample(other_names, min(len(other_names), 3))
        options = wrong_answers + [correct_answer]
        random.shuffle(options)
        st.session_state.options = options

    # පින්තූරය පෙන්වීම
    col1, col2 = st.columns([1, 1])
    with col1:
        if os.path.exists(img_filename):
            st.image(img_filename, use_container_width=True)
        else:
            st.error(f"පින්තූරය හමු නොවීය: {img_filename}")

    with col2:
        st.write(f"### ප්‍රශ්නය {st.session_state.current_index + 1} / {len(image_files)}")
        st.write("**මෙම පින්තූරයේ සිටින්නේ කවුද?**")
        
        choice = st.radio("පිළිතුරක් තෝරන්න:", st.session_state.options, key=f"radio_{img_filename}")
        
        if not st.session_state.answered:
            if st.button("පිළිතුර තහවුරු කරන්න"):
                st.session_state.answered = True
                if choice == correct_answer:
                    st.success(f"නිවැරදියි! ✅ මේ {correct_answer}")
                    st.session_state.score += 1
                else:
                    st.error(f"වැරදියි! ❌ නිවැරදි පිළිතුර: {correct_answer}")
                st.rerun()
        else:
            if st.button("ඊළඟ පින්තූරයට යන්න ➡️"):
                next_question()
                st.rerun()

    st.progress(st.session_state.current_index / len(image_files))

else:
    st.balloons()
    st.header("සෙල්ලම අවසන්! 🎉")
    st.subheader(f"ඔබේ ලකුණු සංඛ්‍යාව: {st.session_state.score} / {len(image_files)}")
    if st.button("නැවත සෙල්ලම් කරන්න"):
        st.session_state.score = 0
        st.session_state.current_index = 0
        st.session_state.options = []
        st.session_state.answered = False
        st.rerun()
