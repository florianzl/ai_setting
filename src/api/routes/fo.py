from fastapi import APIRouter, HTTPException
from src.nlu.fo_client import query_4o
import asyncio

router = APIRouter()

@router.post("/chat/")
async def chat_with_4o(prompt: str):
    """
    Nimmt einen Prompt entgegen und gibt die Antwort von 4o zurück.
    """
    try:
        result = await query_4o(prompt)
        # Hier gehen wir davon aus, dass das Ergebnis in result[0]["generated_text"] enthalten ist.
        # Passe dies an, wenn das Format anders ist.
        answer = result[0].get("generated_text", "Keine Antwort erhalten.")
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
