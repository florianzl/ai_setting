# API-Route für Text-to-Speech

from fastapi import APIRouter

router = APIRouter()

@router.post("/tts/")
def synthesize_speech():
    return {"message": "Speech generated"}
