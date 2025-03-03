# Basis-Image für Apple Silicon (ARM64-kompatibel)
FROM python:3.11-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Systemabhängigkeiten installieren (für Audioverarbeitung)
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Quellcode kopieren
COPY src/ /app/src/

# FastAPI-App starten
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]