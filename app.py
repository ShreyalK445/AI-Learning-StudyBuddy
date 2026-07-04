import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Configure Gemini API

model = genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(page_title=" Shreyal Learning StudyBuddy", page_icon="🎓")
st.title("🎓 Shreyal Learning your StudyBuddy")
topic = st.text_input("Enter a Topic")
option = st.selectbox(
"Choose according to your learning skill",
[
"Explain Concept",
"Real-Life Example",
"Generate Quiz",
"Ask Anything"
]
)
if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic


        response = model.generate_content(prompt)
        st.write(response.text)
