import streamlit as st

# Custom CSS for the layout and styling
st.markdown(
    """
    <style>
    .experience-section {
        padding: 20px;
        margin-bottom: 40px;
        border-bottom: 1px solid #ddd;
    }

    .experience-title {
        font-size: 26px;
        font-weight: bold;
        color: #333;
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }

    .experience-title span {
        margin-left: 10px;
        font-size: 20px;
        color: #888;
    }

    .company-title {
        font-size: 22px;
        color: green;
        font-weight: bold;
    }

    .position-title {
        font-size: 16px;
        color: #555;
        margin-top: 5px;
    }

    .experience-details {
        margin-top: 10px;
        color: #333;
        font-size: 14px;
    }

    .experience-details li {
        margin-bottom: 10px;
    }

    .experience-time-location {
        text-align: right;
        color: #666;
        font-size: 14px;
        margin-top: -40px;
        margin-bottom: 20px;
    }

    .company-website {
        margin-top: 15px;
        display: inline-block;
        padding: 10px 20px;
        border: 1px solid #ddd;
        border-radius: 5px;
        color: #333;
        text-decoration: none;
    }

    .company-website:hover {
        background-color: #f5f5f5;
    }

    .section-header {
        font-size: 32px;
        font-weight: bold;
        color: #333;
        border-bottom: 3px solid;
        border-image: linear-gradient(to right, orange, green, blue) 1;
        display: inline-block;
        padding-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Section
st.markdown('<div class="section-header">Projects 📑</div>', unsafe_allow_html=True)

# Experience 1
st.markdown(
    """
    <div class="experience-section">
        <div class="experience-title">
            <div class="company-title">Wilcmds | Wildcats Innov Lab</div>
            <span>Appdev</span>
        </div>
        <div class="experience-time-location">January 2024</div>
        <ul class="experience-details">
            <li>Wilcmds automate the distribution of educational content, news and updates to startups and stakeholders</li>
            <li>Used Django python and Javascript</li>
            <li>Integrated the Facebook API</li>
        </ul>
        <a href="#https://github.com/hezekiahdane/wilcmds?tab=readme-ov-file" class="company-website">Github</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Experience 2
st.markdown(
    """
    <div class="experience-section">
        <div class="experience-title">
            <div class="company-title" style="color: #06c4b1;">ServiceYou</div>
            <span>Information Management 2</span>
        </div>
        <div class="experience-time-location">August 2023</div>
        <ul class="experience-details">
            <li>Is a web application that facilitates transactions between Clients and Workers, allowing Clients to hire Workers to complete various tasks. The platform also includes a payment system to manage financial transactions.</li>
            <li>Used Django python and HTML.</li>
            <li>Created the transaction part</li>
        </ul>
        <a href="#https://github.com/jmarcbalbada/ServiceYou" class="company-website">Github</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Experience 3
st.markdown(
    """
    <div class="experience-section">
        <div class="experience-title">
            <div class="company-title" style="color: #1a73e8;">MetroEvents</div>
            <span>Full Stack</span>
        </div>
        <div class="experience-time-location">August 2023</div>
        <ul class="experience-details">
            <li>Is a web browser application that tracks events and notifies user</li>
            <li>Used PHP and CSS.</li>
            <li>Created the backend to input and create events for users.</li>
        </ul>
        <a href="#" class="company-website">Github</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Experience 4
st.markdown(
    """
    <div class="experience-section">
        <div class="experience-title">
            <div class="company-title" style="color: #550b87;">TransitPal | Bus Tracker</div>
            <span>Frontend</span>
        </div>
        <div class="experience-time-location">July 2022</div>
        <ul class="experience-details">
            <li>Easily track your bus in real-time, view detailed schedules, and manage your payments all in one place. </li>
            <li>Used Java and Android Studio</li>
        </ul>
        <a href="#https://github.com/RoheinNe/Prj" class="company-website">Github</a>
    </div>
    """,
    unsafe_allow_html=True
)
