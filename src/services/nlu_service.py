# src/services/nlu_service.py
def analyze_text(text: str) -> dict:
    """
    Dummy-NLU: Diese Funktion analysiert den übergebenen Text und extrahiert einen festen Intent
    sowie Beispiel-Entitäten. In einer echten Implementierung würde hier ein NLU-Modell (z. B. DeepSeek oder GPT-basierte Modelle)
    verwendet werden.
    """
    # Beispielhafte Rückgabe: Immer "Termin buchen" als Intent und Beispiel-Daten für Datum und Uhrzeit.
    return {
        "intent": "termin_buchen",
        "entities": {
            "date": "2025-03-10",
            "time": "10:00"
        }
    }
