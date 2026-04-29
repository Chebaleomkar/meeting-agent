import os
import requests
from dotenv import load_dotenv

load_dotenv()
MEETING_ID = os.environ["MEETING_ID"]
API_KEY = os.environ["VEXA_API_KEY"]

response = requests.post(
    "https://api.cloud.vexa.ai/bots",
    headers={
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "platform": "google_meet",
        "native_meeting_id": MEETING_ID,
        "bot_name": "Omkar Agent",
        "language": "en",
        "voice_agent_enabled": True
    }
)
print(response.status_code, response.json())
print("Bot is joining. Admit it from one of your browser tabs.")
