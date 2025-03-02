# src/services/audio_storage.py
from typing import Dict
import uuid

# Einfacher In-Memory-Speicher: audio_id -> audio_bytes
audio_files: Dict[str, bytes] = {}

def store_audio_file(audio_bytes: bytes) -> str:
    """
    Speichert die Audiodatei in einem Dict und gibt eine eindeutige ID zurück.
    """
    audio_id = str(uuid.uuid4())
    audio_files[audio_id] = audio_bytes
    return audio_id

def get_audio_file(audio_id: str) -> bytes:
    """
    Ruft das Audio für eine gegebene ID ab. Falls nicht gefunden, werfen wir eine Exception.
    """
    if audio_id not in audio_files:
        raise FileNotFoundError(f"Audio ID {audio_id} nicht gefunden.")
    return audio_files[audio_id]
