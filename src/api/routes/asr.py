#API-Route für Speech-to-Text

from fastapi import APIRouter

router = APIRouter()

@router.post("/asr/")
def transcribe_audio():
    return {"message": "Audio transcribed"}
