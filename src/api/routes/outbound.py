# src/api/routes/outbound.py

from fastapi import APIRouter
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse, Start, Stream

router = APIRouter()

@router.post("/twilio/outbound")
async def twilio_outbound():
    """
    Twilio ruft diesen Endpunkt, sobald der ausgehende Anruf 
    vom Angerufenen angenommen wird.
    """
    response = VoiceResponse()

    # <Start><Stream> für Media Streams
    start = Start()
    # Ersetze <deine-ngrok-domain> durch den aktiven ngrok-Link
    start.append(Stream(url="wss://ab39-185-115-7-111.ngrok-free.app/ws/twilio-media/"))
    response.append(start)

    response.say("Hallo! Ich bin dein KI-Assistent. Bitte sag mir, was du brauchst.")
    return Response(str(response), media_type="application/xml")
