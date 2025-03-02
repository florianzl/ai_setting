# src/services/tts_service.py

def synthesize_speech(text: str) -> bytes:
    """
    Dummy-TTS: Diese Funktion simuliert die Generierung von Sprachausgabe.
    In einer echten Implementierung würdest du hier z.B. ElevenLabs ansprechen.
    """
    # Wir geben nur einen statischen Byte-String als "Audio" zurück.
    # In der Realität wäre dies das resultierende Audio aus einem TTS-System.
    fake_audio = f"Audio Dummy für den Text: {text}".encode("utf-8")
    return fake_audio