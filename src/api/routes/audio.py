# src/api/routes/audio.py
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from src.services.audio_storage import get_audio_file

router = APIRouter()

@router.get("/audio/{audio_id}", response_class=Response)
async def get_audio(audio_id: str):
    """
    Gibt die Audiodatei (z. B. MP3 oder WAV) zurück. 
    Twilio ruft diese URL auf, wenn wir in unserem TwiML `<Play>` angeben.
    """
    try:
        audio_data = get_audio_file(audio_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Audio not found.")
    # Als Beispiel: Wir gehen davon aus, es wäre eine WAV- oder MP3-Datei. 
    # Für einen Dummy: "audio/mpeg" oder "audio/wav"
    return Response(content=audio_data, media_type="audio/mpeg")
