import streamlit as st
from gtts import gTTS
import time
import os

# Function to create and play audio
def speak_text_gtts(text, lang_code):
    tts = gTTS(text=text, lang=lang_code, slow=False)
    audio_file_path = "output.mp3"
    tts.save(audio_file_path)
    
    # Check if file exists and play audio
    if os.path.exists(audio_file_path):
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
    
    # Add a small delay to allow the file to finish playing before deletion
    time.sleep(1)
    
    try:
        os.remove(audio_file_path)
    except PermissionError as e:
        st.error(f"Error removing file: {e}")

# Streamlit Web Interface
st.title("Test Audio Playback with gTTS")

user_input = st.text_input("Enter Text for Audio Playback", "Hello, this is a test!")
if user_input:
    speak_text_gtts(user_input, lang_code='en')
