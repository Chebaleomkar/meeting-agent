import asyncio
import json
import os
import websockets
from dotenv import load_dotenv

load_dotenv()

MEETING_ID = os.environ["MEETING_ID"]



async def listen():
    async with websockets.connect(
        "wss://api.cloud.vexa.ai/ws",
        additional_headers={"X-API-Key": os.environ["VEXA_API_KEY"]}
    ) as ws:
        await ws.send(json.dumps({
            "action": "subscribe",
            "meetings": [{"platform": "google_meet", "native_id": MEETING_ID}]
        }))
        print("Subscribed. Talk in the meeting and watch this terminal.")

        async for message in ws:
            data = json.loads(message)
            msg_type = data.get("type", "unknown")

            if msg_type == "error":
                print(f"[ERROR] {data}")
            elif msg_type == "subscribed":
                print(f"[OK] Subscribed successfully")
            elif msg_type == "transcript":
                # Confirmed (finalized) segments
                for seg in data.get("confirmed", []):
                    speaker = seg.get("speaker", "Unknown")
                    text = (seg.get("text") or "").strip()
                    if text:
                        print(f"[{speaker}] {text}")
                # Pending (in-progress) segments
                for seg in data.get("pending", []):
                    speaker = seg.get("speaker", "Unknown")
                    text = (seg.get("text") or "").strip()
                    if text:
                        print(f"[{speaker}] (pending) {text}")
            elif msg_type in ("speak.started", "speak.completed", "speak.interrupted"):
                print(f"[BOT] {msg_type}: {data}")
            else:
                print(f"[DEBUG] {msg_type}: {json.dumps(data, indent=2)}")

asyncio.run(listen())