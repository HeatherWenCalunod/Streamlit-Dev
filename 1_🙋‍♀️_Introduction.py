import streamlit as st
from    PIL import Image
from streamlit_navigation_bar import st_navbar

prof = Image.open('assets/prof_pic.jpg')
with open("assets/cv.pdf", "rb") as file:
    resume_data = file.read()

st.set_page_config(
    page_title="Introduction",
    page_icon= ":woman-raising-hand:",
)


st.markdown(
    """
    <style>
    .about-me-section {
        padding: 20px 0;
    }

    .about-me-title {
        font-size: 32px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        position: relative;
    }

    .about-me-title:after {
        content: "";
        display: block;
        width: 100%;
        height: 2px;
        background: linear-gradient(to right, orange, green, blue);
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .about-me-content {
        font-size: 16px;
        color: #555;
    }
  
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="about-me-section">', unsafe_allow_html=True)
st.markdown('<div class="about-me-title">About Me 🙋‍♀️</div>', unsafe_allow_html=True)
col1,spacer, col2 = st.columns([2, 1,1])

with col1:
    st.markdown('<div class="about-me-content">I briefly studied pharmacy, but it wasn’t the right fit for me. I discovered that my true passion lies in coding. I am now pursuing a Bachelor of Science in Information Technology at Cebu Institute of Technology, with an expected graduation date of May 2025.</div>'
    , unsafe_allow_html=True)

st.markdown("###### 👋 Name: Heather Wen L. Calunod")
st.markdown("###### ⏰ Age: 23")
st.markdown("###### 📍 Location: Lawaan 1, Talisay City Cebu")
st.markdown("###### 🏃‍♂️ Hobbies: Design, UI/UX, Baking")
st.markdown("###### 🎨 Favorite Artist: Chappel Roan")
st.write(" ")
st.write(" ")
st.download_button(
    label="Download Resume",
    data=resume_data,
    file_name="resume.pdf",
    mime="application/pdf"
)
st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.image(prof, use_column_width=True)

  
SOCIAL_MEDIA = {
    "Github" : "https://github.com",
    "Email" : "https://www.microsoft.com/en-ph",
    "LinkedIn": "https://linkedin.com",
    "Twitter": "https://twitter.com",


}
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platfrom,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platfrom}]({link})")
st.markdown('</div>', unsafe_allow_html=True)
st.sidebar.success("Select a page above.")

st.video("assets/Mitski.mp4")
