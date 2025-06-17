import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# for Set Gemini key!
genai.configure(api_key=api_key)

# Supported Languages
languages = [
    "Urdu", "French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Arabic",
    "Portuguese", "Russian", "Hindi", "Bengali", "Turkish", "Italian", "Dutch", "Greek",
    "Polish", "Swedish", "Thai", "Pashto", "Hebrew", "Malay", "Czech", "Romanian", "Persion"
]

# Streamlit UI
st.set_page_config(page_title="Translator by Ramisha", layout="centered")
st.title("🌐 AI Translator Agent 🤖🎊")
st.subheader("Created by *Ramisha Tariq*")
st.markdown("–**Translate your English text into diffrent languages by using Gemini AI Features.**")

text = st.text_area("✏Enter English text to translate:", height=130)
lang = st.selectbox("✔ Select your translate language:", languages)
btn = st.button("Translate Now!")

if btn and text:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Translate the following text to {lang}:\n\n{text}"
        response = model.generate_content(prompt)
        st.success(f"✅ Translated to {lang}:")
        st.markdown(f"{response.text}")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
    
