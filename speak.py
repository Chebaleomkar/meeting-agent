import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

MEETING_ID = os.environ["MEETING_ID"]
API_KEY = os.environ["VEXA_API_KEY"]
API_BASE = "https://api.cloud.vexa.ai"

# --- Option 1: TTS (text-to-speech via Vexa) ---
def speak_text(text="Hello team, this is the agent speaking."):
    response = requests.post(
        f"{API_BASE}/bots/google_meet/{MEETING_ID}/speak",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json={"text": text, "provider": "openai", "voice": "nova"}
    )
    print(f"TTS speak: {response.status_code} {response.json()}")

# --- Option 2: Pre-rendered audio via base64 ---
def speak_audio(file_path):
    with open(file_path, "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode()
    response = requests.post(
        f"{API_BASE}/bots/google_meet/{MEETING_ID}/speak",
        headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
        json={"audio_base64": audio_b64, "format": "wav", "sample_rate": 24000, "channels": 1}
    )
    print(f"Audio speak: {response.status_code} {response.json()}")

if __name__ == "__main__":
    # Try TTS first
    speak_text()
    # If TTS doesn't work, generate audio locally and use:
    # speak_audio("greeting.wav")
