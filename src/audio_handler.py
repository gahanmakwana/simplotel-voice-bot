import tempfile
import whisper
from gtts import gTTS
import base64
import os
import sys

# Only add Windows path if running on Windows
if sys.platform == "win32":
    os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"
# Load the base model (small enough for CPU, decent accuracy)
# This downloads about ~140MB the first time you run it.
model = whisper.load_model("base")

def transcribe_audio(audio_bytes):
    # Create a temp file to store audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name
    
    try:
        # Transcribe using local CPU
        result = model.transcribe(tmp_path)
        return result["text"]
    finally:
        # Clean up temp file
        os.unlink(tmp_path)

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        audio_file = tmp.name
        
    with open(audio_file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        
    return f'<audio autoplay src="data:audio/mp3;base64,{b64}"></audio>'