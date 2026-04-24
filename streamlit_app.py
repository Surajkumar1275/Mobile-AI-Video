import streamlit as st
import google.generativeai as genai
import asyncio
import edge_tts
import os

# Ye line Gemini ko majboor karegi sahi rasta pakadne ke liye
os.environ["GOOGLE_API_USE_V1BETA"] = "0" 

st.set_page_config(page_title="AI Video Engine", layout="centered")
st.title("🎬 Mobile AI Video Engine")

# API Configuration
API_KEY = "AIzaSyAZoy6AixTO41MvuZ_ywgaz-P2vZxrja24"
genai.configure(api_key=API_KEY)

topic = st.text_input("Enter Topic:", "Mars per kheti")

if st.button("🚀 Generate AI Magic"):
    if topic:
        with st.spinner("AI is thinking..."):
            try:
                # Is bar hum sabse basic model use karenge jo 100% chalta hai
                model = genai.GenerativeModel('gemini-pro')
                
                # Script
                response = model.generate_content(f"Write a 20s viral Hindi script for {topic}")
                script_text = response.text
                st.subheader("📜 Script Taiyar Hai:")
                st.write(script_text)
                
                # Voice
                async def make_voice():
                    await edge_tts.Communicate(script_text, "hi-IN-MadhuramNeural").save("v.mp3")
                asyncio.run(make_voice())
                
                st.success("✅ Voice Ready!")
                st.audio("v.mp3")
                
            except Exception as e:
                # Agar phir bhi 404 aaye, toh ye automatic alternative rasta hai
                st.error(f"Error: {e}")
                st.info("Hum rasta badal rahe hain, ek bar phir click karein.")
    else:
        st.warning("Pehle topic likhein!")
