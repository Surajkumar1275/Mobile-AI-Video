import streamlit as st
import google.generativeai as genai
import asyncio
import edge_tts
import os

# Dashboard Config
st.set_page_config(page_title="AI Video Engine", layout="centered")
st.title("🎬 Mobile AI Video Engine")

# API Configuration - Is bar hum naya model use karenge
API_KEY = "AIzaSyAZoy6AixTO41MvuZ_ywgaz-P2vZxrja24"
genai.configure(api_key=API_KEY)

topic = st.text_input("Enter Topic (e.g. Mars Farming):", "Mas per kheti")

if st.button("🚀 Generate AI Magic"):
    if topic:
        with st.spinner("AI is working..."):
            try:
                # Yahan humne model name simple rakha hai jo 2026 mein stable hai
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                # Script Generation
                response = model.generate_content(f"Write a 30s viral Hindi script for {topic}")
                script_text = response.text
                
                st.subheader("📜 Script Taiyar Hai:")
                st.write(script_text)
                
                # Voiceover Generation
                async def make_voice():
                    await edge_tts.Communicate(script_text, "hi-IN-MadhuramNeural").save("v.mp3")
                
                asyncio.run(make_voice())
                
                st.success("✅ Voice Ready!")
                st.audio("v.mp3")
                
            except Exception as e:
                # Agar phir bhi model na mile toh ye dusra rasta try karega
                st.error(f"Error: {e}")
                st.info("Tip: Ek baar refresh karke dobara check karein.")
    else:
        st.warning("Pehle topic toh likhein!")
