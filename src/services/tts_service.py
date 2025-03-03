# src/services/tts_service.py
import os
import requests

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "<default_voice_id>")

def synthesize_speech(text: str) -> bytes:
    # ElevenLabs-Endpoint
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()

    # resp.content enthält MP3-Daten
    return resp.content
