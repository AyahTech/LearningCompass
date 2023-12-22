# Import necessary libraries
import streamlit as st
from streamlit_extras.let_it_rain import rain
import time
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Set up the model for chatbot
generation_config = {
    "temperature": 0.6,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Start a chat conversation with predefined history
convo = model.start_chat(
    history=[
        {"role": "user", "parts": "official websites and youtube channels that offer learning materials on python"},
        {
            "role": "model",
            "parts": """### Official Websites:\n\n1. **Python.org:**\n   - The official website of the Python programming language.\n   - Offers comprehensive documentation, tutorials, and resources for learning Python.\n   - Includes a section dedicated to beginners, with interactive tutorials and guides.\n   - Link: [Python.org](https://www.python.org/)\n\n... (remaining content)"""
        },
        {"role": "user", "parts": "official websites and youtube channels that offer learning materials on baking"},
        {
            "role": "model",
            "parts": """### Official Websites:\n\n1. **King Arthur Flour:**\n   - The official website of King Arthur Flour, a leading flour company and baking resource.\n   - Offers a wide range of baking recipes, tutorials, and resources for bakers of all levels.\n   - Includes sections on basic baking techniques, ingredient guides, and troubleshooting tips.\n   - Link: [King Arthur Flour](https://www.kingarthurbaking.com/)\n\n... (remaining content)"""
        },
        {"role": "user", "parts": "official websites and youtube channels that offer learning materials on machine learning"},
        {
            "role": "model",
            "parts": """### Official Websites:\n\n1. **Google Developers Machine Learning:**\n   - The official website of Google's machine learning resources for developers.\n   - Offers comprehensive documentation, tutorials, and guides on machine learning concepts and techniques.\n   - Includes sections on TensorFlow, a popular machine learning library developed by Google.\n   - Link: [Google Developers Machine Learning](https://developers.google.com/machine-learning)\n\n... (remaining content)"""
        },
    ]
)

# Streamlit app layout
st.image("./compass.svg")
st.title("Learning Compass")
st.markdown(
    """
    Welcome to Learning Compass! Embark on your learning journey here with custom learning paths **powered by Gemini**, guiding you towards knowledge and skill mastery tailored just for you.
    """
)

# Display raining emojis
rain(
    emoji="💠",
    font_size=20,
    falling_speed=10,
    animation_length="infinite",
)

# Prompt for user input
prompt = st.chat_input("Enter your learning topic..")
convo.send_message("design a step-by-step learning path with explanations and concepts to cover and provide online resources like names only of websites and YouTube channels on  " + str(prompt))

# Display chatbot response
if prompt:
    with st.chat_message("🧭"):
        st.markdown(convo.last.text)

