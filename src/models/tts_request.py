# src/models/tts_request.py
from pydantic import BaseModel

class TTSRequest(BaseModel):
    text: str
