# Meeting Agent

A Vexa-powered meeting bot that joins Google Meet calls, streams real-time transcripts, and speaks via TTS.

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Install dependencies

```bash
pip install vexa-client websockets requests python-dotenv
```

### 3. Configure environment

Create a `.env` file:

```
VEXA_API_KEY=your_vexa_api_key_here
MEETING_ID=your-meeting-id
```

- Get your API key from [vexa.ai/account](https://vexa.ai/account)
- `MEETING_ID` is the part after `meet.google.com/` in your Google Meet URL (e.g., `abc-defg-hij`)

## Usage

Run the scripts in order:

### Step 1 — Send the bot to your meeting

```bash
python send_bot.py
```

This sends a bot (named "Omkar Agent") to join your Google Meet. Admit it from the meeting when it appears in the waiting room.

### Step 2 — Stream live transcripts

```bash
python listen.py
```

Connects via WebSocket and prints real-time transcripts as people speak in the meeting.

### Step 3 — Make the bot speak

```bash
python speak.py
```

Sends a TTS command to make the bot speak in the meeting. Supports both text-to-speech (via OpenAI) and pre-rendered audio (base64/URL).

## Issue

The `/speak` endpoint returns `202 Accepted` but the bot does not produce any audio in the meeting. Investigating whether `voice_agent_enabled` requires additional account-level configuration.
