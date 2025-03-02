from fastapi import APIRouter
from src.core.logger import logger  # Import des Loggers

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    logger.info("Healthcheck aufgerufen")
    return {"status": "OK"}
