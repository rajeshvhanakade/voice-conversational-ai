# app/ui/app.py

import sys
from pathlib import Path
import streamlit as st

# add app/ to path
APP_DIR = Path(__file__).resolve().parents[1]  # voice_agent/app
if str(APP_DIR) not in sys.path:
    sys.path.append(str(APP_DIR))

from stt.whisper_stt import listen
from tts.tts_engine import speak
from agent.controller import agent_loop

st.set_page_config(page_title="Voice Conversational AI", page_icon="🤖")

st.title("🤖 Voice Conversational AI")
st.write("Press the button, speak, and get AI response!")

if "last" not in st.session_state:
    st.session_state.last = ""

if st.button("🎤 Record Voice", key="record_btn"):
    st.info("Listening...")

    user_text = listen()
    st.write("**You said:**", user_text)

    ai_reply = agent_loop(user_text)
    st.session_state.last = ai_reply

    st.write("**AI:**", ai_reply)
    speak(ai_reply)

if st.session_state.last:
    st.divider()
    st.write("**Last response:**")
    st.write(st.session_state.last)