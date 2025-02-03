from fastapi import FastAPI
from src.api.routes import health

# FastAPI-Anwendung initialisieren
app = FastAPI()

app.include_router(health.router)
