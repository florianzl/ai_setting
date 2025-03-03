# src/api/routes/play_audio.py
from fastapi import APIRouter, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Play

router = APIRouter()

@router.post("/twilio/play_audio/{audio_id}")
async def play_audio(audio_id: str, request: Request):
    response = VoiceResponse()

    # Audio-Datei per GET abrufbar machen
    base_url = f"{request.url.scheme}://{request.url.hostname}"
    if request.url.port:
        base_url += f":{request.url.port}"
    audio_url = f"{base_url}/audio/{audio_id}"

    response.play(audio_url)
    return Response(str(response), media_type="application/xml")
