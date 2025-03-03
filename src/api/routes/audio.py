# src/api/routes/audio.py
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from src.services.audio_storage import get_audio_file

router = APIRouter()

@router.get("/audio/{audio_id}")
async def get_audio_file_route(audio_id: str):
    """
    Liefert die gespeicherte Audiodatei (Dummy-Bytes).
    Twilio ruft diese URL, wenn <Play> diese Datei abspielt.
    """
    try:
        audio_data = get_audio_file(audio_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Audio not found")

    # Dummy: Wir deklarieren es als audio/mpeg
    return Response(content=audio_data, media_type="audio/mpeg")
