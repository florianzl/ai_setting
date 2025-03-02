# src/api/routes/voice.py
from fastapi import APIRouter
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Start, Stream

router = APIRouter()

@router.post("/twilio/voice")
async def twilio_voice():
    response = VoiceResponse()

    # Erstelle ein <Start>-Element mit einem <Stream>-Subelement,
    # das Twilio anweist, einen Media Stream an den WebSocket-Endpunkt zu öffnen.
    start = Start()
    # Ersetze "your-ngrok-domain.ngrok-free.app" durch deine öffentliche ngrok-Domain.
    start.append(Stream(url="wss://ab39-185-115-7-111.ngrok-free.app/ws/twilio-media/"))
    response.append(start)

    # Optional: Begrüßung an den Anrufer
    response.say("Hallo. Wie kann ich dir helfen?")

    return Response(content=str(response), media_type="application/xml")
