A voice-enabled AI receptionist that can check room availability, answer hotel policy FAQs, and make real-time bookings into a SQLite database.

## 🚀 Features
- **Voice-to-Voice Interaction:** Speak naturally to the bot.
- **Real-time Database:** Checks actual room inventory in `data/hotel.db`.
- **Zero-Cost Architecture:** Uses local Whisper (STT) and Groq Llama 3.1 (LLM) API.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Model:** Llama 3.1-8b (via Groq API)
- **Speech-to-Text:** OpenAI Whisper (Local Base Model)
- **Text-to-Speech:** gTTS (Google Text-to-Speech)
- **Database:** SQLite

## ⚙️ Setup Instructions

1. **Install FFmpeg** (Required for audio processing):
   - Windows: `winget install Gyan.FFmpeg`

2. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt# Simplotel Voice Concierge 🏨

A voice-enabled AI receptionist that can check room availability, answer hotel policy FAQs, and make real-time bookings into a SQLite database.

## 🚀 Features
- **Voice-to-Voice Interaction:** Speak naturally to the bot.
- **Real-time Database:** Checks actual room inventory in `data/hotel.db`.
- **Zero-Cost Architecture:** Uses local Whisper (STT) and Groq Llama 3.1 (LLM) API.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Model:** Llama 3.1-8b (via Groq API)
- **Speech-to-Text:** OpenAI Whisper (Local Base Model)
- **Text-to-Speech:** gTTS (Google Text-to-Speech)
- **Database:** SQLite

## ⚙️ Setup Instructions

1. **Install FFmpeg** (Required for audio processing):
   - Windows: `winget install Gyan.FFmpeg`

2. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt# Simplotel Voice Concierge 🏨

A voice-enabled AI receptionist that can check room availability, answer hotel policy FAQs, and make real-time bookings into a SQLite database.

## 🚀 Features
- **Voice-to-Voice Interaction:** Speak naturally to the bot.
- **Real-time Database:** Checks actual room inventory in `data/hotel.db`.
- **Zero-Cost Architecture:** Uses local Whisper (STT) and Groq Llama 3.1 (LLM) API.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Model:** Llama 3.1-8b (via Groq API)
- **Speech-to-Text:** OpenAI Whisper (Local Base Model)
- **Text-to-Speech:** gTTS (Google Text-to-Speech)
- **Database:** SQLite

## ⚙️ Setup Instructions

1. **Install FFmpeg** (Required for audio processing):
   - Windows: `winget install Gyan.FFmpeg`

2. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt

3. Setup Environment Variables: Create a .env file:
    GROQ_API_KEY=your_groq_api_key_here

4. Initialize Database:
    python seed_db.py

5. Run the App:
    streamlit run app.py

---
