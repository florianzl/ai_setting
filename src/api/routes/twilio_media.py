from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from twilio.twiml.voice_response import VoiceResponse
import json
import base64
import os
from twilio.rest import Client
from src.services.asr_service import transcribe_audio
from src.services.nlu_service import analyze_text
from src.services.tts_service import synthesize_speech
from src.services.audio_storage import store_audio_file
from dotenv import load_dotenv

# Lade Umgebungsvariablen
load_dotenv()

router = APIRouter()

# Umgebungsvariablen
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
NGROK_URL = os.getenv("NGROK_URL")

# Neuer TwiML-Endpunkt
@router.post("/twilio/outbound")
async def twilio_outbound():
    response = VoiceResponse()
    response.say("Hallo! Ich bin dein KI-Assistent.", voice="Polly.Hans", language="de-DE")
    # Verlinkt den WebSocket für Medienströme
    response.connect().stream(url=f"wss://{NGROK_URL.split('https://')[1]}/ws/twilio-media/")
    return str(response)

# Bestehender WebSocket-Endpunkt
@router.websocket("/ws/twilio-media/")
async def twilio_media_ws(websocket: WebSocket):
    await websocket.accept()
    call_sid = None
    audio_chunks = []  # Sammle Chunks für realistischere Transkription

    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            event = msg.get("event", "")

            if event == "start":
                start_info = msg.get("start", {})
                call_sid = start_info.get("callSid")
                print(f"Media Stream gestartet für Call: {call_sid}")

            elif event == "media":
                payload = msg.get("media", {}).get("payload", "")
                audio_bytes = base64.b64decode(payload)
                # Optional: Teiltranskription hier möglich
                audio_chunks.append(audio_bytes)  # Sammle Chunks

            elif event == "stop":
                print("Media Stream beendet:", msg)
                # Kombiniere alle Chunks und transkribiere
                full_audio = b''.join(audio_chunks)
                transcription = await transcribe_audio(full_audio)
                print("ASR-Transkription:", transcription)

                # NLU (noch Dummy)
                nlu_result = analyze_text(transcription)
                print("NLU:", nlu_result)

                # TTS: Antwort generieren
                final_answer = "Dein Termin wurde gebucht. Vielen Dank und auf Wiederhören!"
                tts_audio = synthesize_speech(final_answer)
                audio_id = store_audio_file(tts_audio)

                # Twilio-Update
                if call_sid:
                    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                    new_url = f"{NGROK_URL}/twilio/play_audio/{audio_id}"
                    client.calls(call_sid).update(url=new_url, method="POST")
                break

    except WebSocketDisconnect:
        print("WebSocket Verbindung getrennt.")