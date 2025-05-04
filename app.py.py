import streamlit as st
import os
from PIL import Image

# Folder path jahan images hain (1.jpg se 30.jpg)
PHOTO_FOLDER = "images"

# Shayari + Quotes list
shayaris = [
    "Tum naraz ho, dil udaas hai,\nTere bina yeh saans bhi kuch khaas nahi hai.",
    "Jab tum naraz hoti ho to lagta hai duniya khali si hai,\nBas ek muskurahat chahiye sab kuch theek ho jaane ke liye.",
    "Dil se nikli har ek baat mein sirf tum ho,\nMeri har khushi, har dua mein tum ho.",
    "Sorry jaan... galti hui, par pyaar wahi hai jo shuru mein tha – pure aur tumse hi juda.",
    "Tum meri duniya ho, meri har dua mein tum ho,\nPlease wapas aa jao, khushiyaan adhoori hain tumhare bina.",
    "Mujhe har roz tumse pyaar karne ka ek naya reason milta hai ❤️"
]

quotes = [
    "“Real love means never having to say you're sorry... but I will, a thousand times.”",
    "“The best apology is changed behavior – I promise to prove that.”",
    "“I hurt you unknowingly, but I love you endlessly.”",
    "“You’re not just my love, you’re my future wife. I’m sorry, meri jaan.”",
    "“Zindagi ka har pal tumhare bina bekar hai... Mujhe maaf karke ek mauka do.”"
]

# Page setup
st.set_page_config(page_title="Sorry My Future Wife ❤️", layout="centered", page_icon="💌")
st.markdown("<h1 style='text-align: center; color: red;'>Hello Dear Anshika ❤️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: hotpink;'>Sorry na babe... I mean Future Wife ❤️</h3>", unsafe_allow_html=True)

# Session state to track page
if "page" not in st.session_state:
    st.session_state.page = 1

# Total pages
TOTAL_PAGES = 6
IMAGES_PER_PAGE = 6

# Get photo files sorted
photo_files = sorted(
    [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
)

# Show 6 images per page
start_index = (st.session_state.page - 1) * IMAGES_PER_PAGE
end_index = start_index + IMAGES_PER_PAGE

if st.session_state.page <= 5:
    st.markdown(f"<h4 style='text-align: center;'>💖 Page {st.session_state.page} of 6 💖</h4>", unsafe_allow_html=True)
    columns = st.columns(3)

    for i, file in enumerate(photo_files[start_index:end_index]):
        img_path = os.path.join(PHOTO_FOLDER, file)
        image = Image.open(img_path)
        with columns[i % 3]:
            st.image(image, use_column_width='auto')

    # Show random shayari or quote
    import random
    message = random.choice(shayaris + quotes)
    st.markdown(
        f"<div style='text-align: center; font-size: 20px; color: blue;'>{message.replace(chr(10), '<br>')}</div>",
        unsafe_allow_html=True
    )

    # Next button
    if st.button("Next ➡️"):
        if st.session_state.page < TOTAL_PAGES:
            st.session_state.page += 1
        else:
            st.session_state.page = 6

# Final Page (Page 6)
elif st.session_state.page == 6:
    st.markdown("<h2 style='text-align: center; color: red;'>💖 Final Page 💖</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; font-size: 22px; color: hotpink; margin-top: 30px;'>
            I love you my dear Anshika ❤️<br>
            Shahgarh ki don, babe, baby — my everything!<br><br>
            Tum aise udaas mat raha karo,<br>
            Mai aapka hone wala hubby hu...<br>
            Aur aap meri hone wali wife ho 💍<br><br>

            Tumhara gussa mujhe tod deta hai,<br>
            Lekin tumhari ek muskurahat meri har takleef mita deti hai.<br>
            Har subah tumse shuru ho aur har raat tum par khatam,<br>
            Yeh meri bas ek hi dua hai zindagi bhar ke liye.<br>
            Tum bas hamesha haste rehna, baaki sab mai sambhal lunga. ❤️
        </div>
        """,
        unsafe_allow_html=True
    )
