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

async def edit_message(
    chat_id: int, 
    text: str, 
    message_id: int,
    reply_markup: dict | None = None
):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "message_id": message_id
    }
    
    if reply_markup:
        payload["reply_markup"] = reply_markup
        
    if http.http_client is None:
        raise RuntimeError("HTTP client has not been initialized.")

    try:
        res = await http.http_client.post(
            f"{settings.TELEGRAM_BOT_API}/editMessageText",
            json=payload
        )

        res.raise_for_status()

    except HTTPError:
        logger.exception("Telegram API request failed.")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Unable to communicate with Telegram."
        )

async def answer_callback_query(callback_query_id: int):
    payload = {
        "callback_query_id": callback_query_id
    }
        
    if http.http_client is None:
        raise RuntimeError("HTTP client has not been initialized.")

    try:
        res = await http.http_client.post(
            f"{settings.TELEGRAM_BOT_API}/answerCallbackQuery",
            json=payload
        )

        res.raise_for_status()

        result = res.json()
        
        if not result.get("ok"):
            logger.error("Telegram rejected callback.")
            
    except HTTPError:
        logger.exception("Failed to acknowledge Telegram callback.")
        raise