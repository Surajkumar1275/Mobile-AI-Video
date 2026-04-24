import streamlit as st
import google.generativeai as genai
import asyncio
import edge_tts

# API Configuration
API_KEY = "AIzaSyAZoy6AixTO41MvuZ_ywgaz-P2vZxrja24"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="AI Video Engine", layout="centered")
st.title("🎬 Mobile AI Video Engine")

topic = st.text_input("Enter Topic (e.g. Life in 2050):", "Future 2050")

if st.button("🚀 Generate AI Magic"):
    if topic:
        with st.spinner("Gemini is writing script..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                res = model.generate_content(f"Write a 30s viral Hindi script for {topic}")
                st.subheader("📜 Script:")
                st.write(res.text)
                
                async def make_voice():
                    await edge_tts.Communicate(res.text, "hi-IN-MadhuramNeural").save("v.mp3")
                asyncio.run(make_voice())
                
                st.success("✅ Voice Ready!")
                st.audio("v.mp3")
            except Exception as e:
                st.error(f"Error: {e}")
