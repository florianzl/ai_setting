# src/api/routes/play_demo.py
from fastapi import APIRouter, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Play
from src.services.tts_service import synthesize_speech
from src.services.audio_storage import store_audio_file

router = APIRouter()

@router.post("/twilio/play_demo")
async def play_demo(request: Request):
    """
    Twilio ruft diesen Endpunkt auf, wenn ein Anruf bei der zugewiesenen Nummer eingeht.
    Wir generieren ein Audio, speichern es und geben eine TwiML-Antwort mit <Play> zurück.
    """
    # 1. Dummy: Erzeuge einen Beispieltext.
    answer_text = "Willkommen beim KI-Agenten. Dies ist eine Dummy-Audioantwort."

    # 2. TTS generieren (Dummy oder echter TTS).
    audio_bytes = synthesize_speech(answer_text)

    # 3. In-Memory speichern, ID zurückbekommen.
    audio_id = store_audio_file(audio_bytes)

    # 4. TwiML erzeugen
    response = VoiceResponse()
    # Twilio ruft die URL unter /audio/{audio_id} ab, um die Audiodatei abzuspielen
    audio_url = f"{request.url.scheme}://{request.url.host}{':' + str(request.url.port) if request.url.port else ''}/audio/{audio_id}"

    response.play(audio_url)
    return Response(content=str(response), media_type="application/xml")
