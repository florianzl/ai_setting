# src/api/routes/nlu.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.nlu_service import analyze_text

class NLURequest(BaseModel):
    text: str

router = APIRouter()

@router.post("/nlu", tags=["NLU"])
async def nlu_analysis(request: NLURequest):
    """
    Diese Route analysiert den eingegebenen Text und gibt einen Dummy-Intent mit Beispieldaten zurück.
    """
    try:
        result = analyze_text(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
