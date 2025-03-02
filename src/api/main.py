# src/api/main.py
from fastapi import FastAPI
from src.core.config import config
from src.core.logger import logger
from src.api.routes.health import router as health_router  # falls vorhanden
from src.api.routes.voice import router as voice_router
from src.api.routes.twilio_media import router as twilio_media_router
from src.api.routes.audio import router as audio_router

app = FastAPI(title="Booking AI Agent", version="0.1.0")

# Einbinden der relevanten Routen
app.include_router(health_router)
app.include_router(voice_router)
app.include_router(twilio_media_router)
app.include_router(audio_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config.API_PORT)
