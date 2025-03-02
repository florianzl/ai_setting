# src/api/routes/twilio_media.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
import base64
from src.services.asr_service import transcribe_audio
from src.services.nlu_service import analyze_text
from src.services.tts_service import synthesize_speech  # Dummy-TTS

router = APIRouter()

@router.websocket("/ws/twilio-media/")
async def twilio_media_ws(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            event = msg.get("event", "")
            
            if event == "start":
                print("Media Stream gestartet:", msg)

            elif event == "media":
                # 1. ASR
                payload = msg.get("media", {}).get("payload", "")
                audio_bytes = base64.b64decode(payload)
                transcription = transcribe_audio(audio_bytes)
                print("ASR Transkription:", transcription)
                
                # 2. NLU
                nlu_result = analyze_text(transcription)
                print("NLU Analyse:", nlu_result)

                # 3. Antwort generieren (Dummy-Logik)
                #    Beispiel: "Ich verstehe, du möchtest einen Termin buchen!"
                answer_text = f"Ich habe erkannt, dass du den Intent '{nlu_result['intent']}' hast!"

                # 4. TTS
                tts_audio = synthesize_speech(answer_text)
                print("TTS Audio (Dummy):", tts_audio)

                # Hier fehlt noch der Schritt, das Audio zurück ans Telefon zu schicken.
            
            elif event == "stop":
                print("Media Stream beendet:", msg)
                break

    except WebSocketDisconnect:
        print("WebSocket-Verbindung getrennt")
