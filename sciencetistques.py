import streamlit as st
import os

st.set_page_config(page_title="ලෝක ප්‍රකට පුද්ගලයින්", page_icon="💡")

st.title("💡 ලෝක ප්‍රකට පුද්ගලයින් කවුද?")
st.write("පින්තූරය බලා නිවැරදි නම සිංහලෙන් හෝ ඉංග්‍රීසියෙන් ඇතුළත් කරන්න.")

# GitHub එකේ පින්තූර තියෙන තැන (Root directory එකේ නිසා හිස්ව තබන්න)
IMAGE_FOLDER = ""

# පින්තූර සහ පිළිතුරු ලැයිස්තුව
data = {
    "1": ["Albert Einstein", "ඇල්බට් අයින්ස්ටයින්"],
    "4": ["Thomas Edison", "තෝමස් එඩිසන්"],
    "7": ["Marie Curie", "මාරි කියුරි"],
    "8": ["Isaac Newton", "අයිසැක් නිව්ටන්"],
    "9": ["Nikola Tesla", "නිකොලා ටෙස්ලා"],
    "10": ["Charles Darwin", "චාල්ස් ඩාවින්"],
    "11": ["Alexander Graham Bell", "ඇලෙක්සැන්ඩර් ග්‍රැහැම් බෙල්"],
    "12": ["Galileo Galilei", "ගැලීලියෝ ගැලිලි"],
    "13": ["Wright Brothers", "රයිට් සහෝදරයෝ"],
    "14": ["Leonardo da Vinci", "ලියනාඩෝ ඩා වින්චි"],
    "15": ["Michael Faraday", "මයිකල් ෆැරඩේ"],
    "17": ["Stephen Hawking", "ස්ටීවන් හෝකින්"],
    "18": ["Benjamin Franklin", "බෙන්ජමින් ෆ්‍රැන්ක්ලින්"],
    "19": ["Louis Pasteur", "ලුවී පාස්චර්"],
    "20": ["Steve Jobs", "ස්ටීව් ජොබ්ස්"]
}

# Session state එක හරියට හදාගමු
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

image_files = list(data.keys())

# ඊළඟ පින්තූරයට යාම සඳහා Function එකක්
def next_question():
    st.session_state.current_index += 1
    st.session_state.answered = False

if st.session_state.current_index < len(image_files):
    img_filename = image_files[st.session_state.current_index]
    correct_answers = data[img_filename]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if os.path.exists(img_filename):
            st.image(img_filename, use_container_width=True)
        else:
            st.error(f"පින්තූරය පේන්න නැහැ: '{img_filename}'")
    
    with col2:
        st.write(f"### ප්‍රශ්න අංකය: {st.session_state.current_index + 1} / {len(image_files)}")
        user_input = st.text_input("මෙයා කවුද?", key=f"input_{st.session_state.current_index}")
        
        # පිළිතුර පරීක්ෂා කිරීමේ බටන් එක
        if st.button("පිළිතුර පරීක්ෂා කරන්න"):
            st.session_state.answered = True
            if any(ans.lower().strip() == user_input.lower().strip() for ans in correct_answers):
                st.success(f"නිවැරදියි! මේ {correct_answers[0]}")
                st.session_state.score += 1
            else:
                st.error(f"වැරදියි. නිවැරදි පිළිතුර: {correct_answers[0]}")
        
        # පිළිතුර දීලා ඉවර නම් පමණක් "ඊළඟ පින්තූරය" බටන් එක පෙන්වන්න
        if st.session_state.answered:
            st.button("ඊළඟ පින්තූරය ➡️", on_click=next_question)

    st.progress(st.session_state.current_index / len(image_files))

else:
    st.balloons()
    st.header("සෙල්ලම අවසන්! 🎉")
    st.subheader(f"ඔබේ ලකුණු ප්‍රමාණය: {st.session_state.score} / {len(image_files)}")
    if st.button("නැවත මුල සිට ආරම්භ කරන්න"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()
