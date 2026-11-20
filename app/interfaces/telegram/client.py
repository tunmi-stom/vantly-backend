from fastapi import HTTPException, status
from httpx import HTTPError
from app.core import http
from app.core.config import settings
from app.core.logging import logger

async def send_message(
    chat_id: int, 
    text: str, 
    reply_markup: dict | None = None
):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    
    if reply_markup:
        payload["reply_markup"] = reply_markup
        
    if http.http_client is None:
        raise RuntimeError("HTTP client has not been initialized.")

    try:
        res = await http.http_client.post(
            f"{settings.TELEGRAM_BOT_API}/sendMessage",
            json=payload
        )

        res.raise_for_status()

    except HTTPError:
        logger.exception("Telegram API request failed.")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Unable to communicate with Telegram."
        )