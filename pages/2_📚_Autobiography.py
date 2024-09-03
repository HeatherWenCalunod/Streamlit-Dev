import streamlit as st
import pydeck as pdk

st.markdown(
    """
    <style>
    /* Adjust the main container to remove padding */
    .main {
        padding: 0px !important;
        margin: 0px !important;
    }

    /* Align the about-me section to the far left */
    .about-me-section {
        padding: 0px !important;
        margin: 0px !important;
        width: 100% !important;
    }

    /* Align the title to the far left */
    .about-me-title {
        font-size: 32px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        margin-left: 0px !important;
        position: relative;
    }

    /* Title underline with gradient */
    .about-me-title:after {
        content: "";
        display: block;
        width: 100%; /* Full width */
        height: 2px;
        background: linear-gradient(to right, orange, green, blue);
        margin-top: 15px;
        margin-bottom: 10px;
    }

    /* Align the content text to the far left */
    .about-me-content {
        font-size: 16px;
        color: #555;
        margin-left: 0px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the content
st.markdown('<div class="about-me-section">', unsafe_allow_html=True)
st.markdown('<div class="about-me-title">Autobiography📚</div>', unsafe_allow_html=True)
st.markdown('<div class="about-me-content">My name is Heather Wen L. Calunod. I am 23yrs old. Living in Lawaan 1, Talisay City Cebu. I have live<br>all my life here.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

latitude_center = 10.2833
longitude_center = 123.85

deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=latitude_center,
        longitude=longitude_center,
        zoom=12,
        pitch=0
    ),
    layers=[]  # No layers for just a map view
)
st.pydeck_chart(deck)

# Render the map in Streamlit
education_history = """
- **Current** – Cebu Institute of Technology University (BS Information Technology)
- **2018-2020** – Asian College of Technology Bulacao Campus (TVL – Home Economics in Baking and Pastry)
- **2011-2018** – Cebu Sacred Heart College
- **2009-2011** – Lawaan Elementary School
- **2007-2009** – Virgen de las Escuelas Pias
"""

novel = """
- **Omniscient Reader's Viewpoint** 
- **Trash of the Count's Family** 
- **Grandmaster of Demonic Cultivation** 
- **The Scum Villain'S Self-Saving System (Mo Xiang Tong Xiu)** 
- **Little Mushroom: Judgment Day** 
"""

st.write(" ")
st.write(" ")
st.markdown('<div class="about-me-section">', unsafe_allow_html=True)
st.markdown('<div class="about-me-title">Educational Background📑</div>', unsafe_allow_html=True)
st.markdown(education_history)
st.markdown('</div>', unsafe_allow_html=True)

st.write(" ")
st.write(" ")
st.markdown('<div class="about-me-section">', unsafe_allow_html=True)
st.markdown('<div class="about-me-title">Favorite Novel📖</div>', unsafe_allow_html=True)
st.markdown(novel)
st.markdown('</div>', unsafe_allow_html=True)
st.write(" ")

line = """
 **** 
"""

st.markdown(line)




st.image("assets/dog.jpg", caption="Sunrise by the mountains")


st.image("assets/brother.jpg", caption="Sunrise by the mountains")


st.image("assets/family.jpg", caption="Sunrise by the mountains")

