from fastapi import APIRouter, Header, HTTPException, Request, status, Depends
import json
from app.core.config import settings
from app.core.logging import logger
from .dispatcher import dispatch
from app.core.database.dependency import db_dependency

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(
    request: Request,
    db: db_dependency,
    x_telegram_bot_api_secret_token: str = Header(None)
):
    # Validate Telegram's webhook secret.
    if x_telegram_bot_api_secret_token != settings.BOT_WEBHOOK_SECRET:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Webhook Secret"
        )
    try:
        # Extract the update.
        update = await request.json()
        
        logger.info("Update received.")
        
        # Pass the above param(update) to each of its dispatcher.
        await dispatch(db, update)
        
    except json.JSONDecodeError as json_err:
        logger.error("Invalid JSON Update Payload: %s", json_err)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid JSON Update Payload."
        )
        
    except Exception as err:
        logger.error("Error Dispatching update: %s", err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error dispatching update"
        )
    
    return {
        "ok": True
    }