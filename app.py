import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Shreyal StudyBuddy Pro", 
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19 !important;
    }
    
    .platform-tag {
        background-color: rgba(59, 130, 246, 0.15);
        color: #60a5fa;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 4px 10px;
        border-radius: 6px;
        border: 1px solid rgba(59, 130, 246, 0.25);
        display: inline-block;
        margin-bottom: 12px;
    }
    
    .stTextInput div div input, .stSelectbox div div div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        color: #f8fafc !important;
        border-radius: 10px !important;
    }
    
    div.stButton > button:first-child {
        width: 100% !important;
        padding: 12px !important;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-1px);
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%) !important;
    }
    
    .status-bar {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.9rem;
        font-weight: 600;
        color: #34d399;
        margin-top: 30px;
        margin-bottom: 12px;
    }
    .green-dot {
        width: 8px;
        height: 8px;
        background-color: #34d399;
        border-radius: 50%;
        display: inline-block;
    }

    .notebook-panel {
        background-color: rgba(19, 27, 46, 0.8);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    study_model = genai.GenerativeModel("gemini-2.5-flash")
except KeyError:
    st.error("Setup Error: Please configure your GEMINI_API_KEY inside Streamlit Secrets.")
    st.stop()

st.markdown('<div class="platform-tag">Learning Module</div>', unsafe_allow_html=True)
st.title("🎓 Shreyal StudyBuddy")
st.write("An intelligent knowledge platform configured to convert complex technical ideas into clear academic modules.")
st.divider()

topic = st.text_input("Target Study Subject / Topic", placeholder="e.g., Photosynthesis, Object-Oriented Principles...")

option = st.selectbox(
    "Choose according to your learning skill",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate Study Module"):
    if not topic.strip():
        st.warning("Please type a topic first.")
    else:
        if option == "Explain Concept":
            prompt = f"Explain the concept of '{topic}' in simple language using clear headings and helpful bullet points."
        elif option == "Real-Life Example":
            prompt = f"Provide a practical real-world scenario or analogy explaining how '{topic}' works simply."
        elif option == "Generate Quiz":
            prompt = f"Create a structured 5-question multiple choice quiz on '{topic}' with a hidden answer key at the bottom."
        else:
            prompt = topic

        with st.spinner("Analyzing parameters... Generating your workspace..."):
            try:
                response = study_model.generate_content(prompt)
                
                st.markdown("""
                    <div class="status-bar">
                        <span class="green-dot"></span>
                        <span>Module Verified & Compiled</span>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="notebook-panel">
                        <h3 style="margin:0; color:#fff;">Workspace Overview: {topic}</h3>
                        <p style="margin:4px 0 0 0; color:#60a5fa; font-size:0.85rem; font-weight:600;">VECTOR: {option}</p>
                        <hr style="border: 0; border-top: 1px solid #334155; margin-top: 15px; margin-bottom: 15px;">
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(response.text)
                
            except Exception as error:
                st.error(f"Something went wrong while running the model: {error}")
