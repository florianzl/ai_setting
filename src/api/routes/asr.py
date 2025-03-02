# src/api/routes/asr.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from src.services.asr_service import transcribe_audio

router = APIRouter()

@router.post("/asr", tags=["ASR"])
async def speech_to_text(file: UploadFile = File(...)):
    """
    Diese Route empfängt eine Audiodatei und liefert eine Transkription zurück.
    """
    try:
        audio_bytes = await file.read()
        transcription = transcribe_audio(audio_bytes)
        return {"transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
