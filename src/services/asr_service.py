# src/services/asr_service.py
import os
from deepgram import DeepgramClient, PrerecordedOptions
from dotenv import load_dotenv

# Lade Umgebungsvariablen
load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Deepgram Client initialisieren
dg_client = DeepgramClient(api_key=DEEPGRAM_API_KEY)

async def transcribe_audio(audio_data: bytes) -> str:
    """
    Nutzt Deepgram, um Audio in Text umzuwandeln.
    Audio-Format: LINEAR_PCM, 16 kHz, Mono (Twilio-kompatibel)
    """
    try:
        options = PrerecordedOptions(
            model="nova-2",
            language="de-DE",
            smart_format=True
        )
        response = await dg_client.transcription.prerecorded(
            {"buffer": audio_data, "mimetype": "audio/wav"},
            options
        )
        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        return transcript if transcript else "Keine Transkription verfügbar"
    except Exception as e:
        print(f"Fehler bei Deepgram ASR: {e}")
        return ""