from fastapi import APIRouter, Header, HTTPException, Request, status
from app.core.config import settings
from app.core.logging import logger
from .dispatcher import dispatch

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(
    request: Request,
    x_telegram_bot_api_secret_token: str = Header(None)
):
    logger.info(
        "Received webhook secret header: %s",
        bool(x_telegram_bot_api_secret_token)
    )

    logger.info(
        "Configured webhook secret: %s",
        bool(settings.BOT_WEBHOOK_SECRET)
    )

    logger.info(
        "Webhook secrets match: %s",
        x_telegram_bot_api_secret_token == settings.BOT_WEBHOOK_SECRET
    )
    # Validate Telegram's webhook secret.
    if x_telegram_bot_api_secret_token != settings.BOT_WEBHOOK_SECRET:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Webhook Secret"
        )
    # Extract the update.
    update = await request.json()
    
    # Pass the above param(update) to each of its dispatcher.
    await dispatch(update)
    return {
        "ok": True
    }