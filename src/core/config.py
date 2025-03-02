# src/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Lädt Variablen aus der .env-Datei

class Config:
    API_PORT = int(os.getenv("API_PORT", 8000))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    # Weitere Konfigurationen (z. B. API-Keys) können hier ergänzt werden.

config = Config()
