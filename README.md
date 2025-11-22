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

### Step 4: Prepare for "How does it work?" Questions
If this is for an interview, here is the "Architecture Explanation" you should memorize:

> "I built a modular AI agent. When I speak, **Streamlit** captures the audio and passes it to a local **Whisper model** running on my CPU to transcribe it to text.
>
> That text is sent to **Llama 3.1 (via Groq)**. I gave the LLM 'tools' (functions) that let it query the **SQLite database** directly. It decides *if* it needs to check availability or book a room, runs the SQL query, and generates a natural language response based on the data.
>
> Finally, **gTTS** converts that text back to audio for the response."

---

### Step 5: Clean Up for Submission
**Do not zip the `venv` folder!** It is huge and contains thousands of unnecessary files.

1.  Delete the `__pycache__` folders if you see them.
2.  Select only:
    * `app.py`
    * `seed_db.py`
    * `requirements.txt`
    * `README.md`
    * The `src` folder
    * The `data` folder
3.  Right-click -> **Send to** -> **Compressed (zipped) folder**.
4.  Name it `Simplotel_Assignment_Krunal.zip`.