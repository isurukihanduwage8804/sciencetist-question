import streamlit as st
import os

# ඇප් එකේ මූලික සැකසුම්
st.set_page_config(page_title="ලෝක ප්‍රකට පුද්ගලයින්", page_icon="💡")

st.title("💡 ලෝක ප්‍රකට පුද්ගලයින් කවුද?")
st.write("පින්තූරය බලා නිවැරදි නම සිංහලෙන් හෝ ඉංග්‍රීසියෙන් ඇතුළත් කරන්න.")

# දැන් පින්තූර තියෙන්නේ ප්‍රධාන තැනම නිසා (No folder)
# IMAGE_FOLDER එක හිස්ව තබමු
IMAGE_FOLDER = ""

# ඔයා GitHub එකට දාපු ෆයිල් වල නම් සහ පිළිතුරු
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

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

image_files = list(data.keys())

if st.session_state.current_index < len(image_files):
    img_filename = image_files[st.session_state.current_index]
    correct_answers = data[img_filename]
    
    # පින්තූරය පෙන්වීම
    img_path = img_filename # ෆෝල්ඩරයක් නැති නිසා කෙලින්ම ෆයිල් නම ගන්නවා
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            # පින්තූරය පේන්නේ නැත්නම් මෙතනින් ඒක කියනවා
            st.error(f"පින්තූරය පේන්න නැහැ: '{img_filename}'")
            st.info("GitHub එකේ මේ නමින්ම ෆයිල් එක තියෙනවා නේද කියලා බලන්න.")
    
    with col2:
        st.write(f"### ප්‍රශ්න අංකය: {st.session_state.current_index + 1} / {len(image_files)}")
        user_input = st.text_input("මෙයා කවුද?", key=f"input_{st.session_state.current_index}")
        
        if st.button("පිළිතුර පරීක්ෂා කරන්න"):
            if any(ans.lower().strip() == user_input.lower().strip() for ans in correct_answers):
                st.success(f"නිවැරදියි! මේ {correct_answers[0]}")
                st.session_state.score += 1
            else:
                st.error(f"වැරදියි. නිවැරදි පිළිතුර: {correct_answers[0]}")
            
            # මීළඟට යාමට Button එක
            if st.button("ඊළඟ පින්තූරය ➡️"):
                st.session_state.current_index += 1
                st.rerun()

    st.progress(st.session_state.current_index / len(image_files))

else:
    st.balloons()
    st.header("සෙල්ලම අවසන්! 🎉")
    st.subheader(f"ඔබේ ලකුණු ප්‍රමාණය: {st.session_state.score} / {len(image_files)}")
    if st.button("නැවත මුල සිට ආරම්භ කරන්න"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.rerun()
