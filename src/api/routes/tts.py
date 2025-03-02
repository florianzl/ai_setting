# src/api/routes/tts.py
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from src.models.tts_request import TTSRequest
from src.services.tts_service import synthesize_speech

router = APIRouter()

@router.post("/tts", tags=["TTS"])
async def text_to_speech(request: TTSRequest):
    """
    Diese Route empfängt Text und gibt einen Audio-Stream zurück, der den synthetisierten Ton enthält.
    """
    try:
        audio_bytes = synthesize_speech(request.text)
        # StreamingResponse erlaubt es, Audio-Daten in einem Stream zurückzugeben.
        return StreamingResponse(iter([audio_bytes]), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
