import os

if not os.path.exists("data/hotel.db"):
    import seed_db
import streamlit as st
from src import audio_handler, bot_logic

st.title("Simplotel Voice Concierge")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful Hotel Concierge for Simplotel. You only answer questions about hotel rooms, bookings, and policies. If a user asks about general topics (like math, history, or code), politely refuse and steer them back to hotel topics."}]

audio_file = st.audio_input("Speak your request")

if audio_file:
    audio_bytes = audio_file.read()
    user_text = audio_handler.transcribe_audio(audio_bytes)
    st.session_state.messages.append({"role": "user", "content": user_text})

    response = bot_logic.chat_with_llm(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response.content})

    st.chat_message("user").write(user_text)
    st.chat_message("assistant").write(response.content)

    st.markdown(audio_handler.text_to_speech(response.content), unsafe_allow_html=True)
