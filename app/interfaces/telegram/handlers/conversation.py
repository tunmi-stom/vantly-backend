from sqlalchemy.orm import Session
from app.interfaces.telegram.client import send_message
from app.services.telegram_session_service import TelegramSessionService

from .start import (
    process_registration_email,
    process_login_email,
    process_login_pass_key
)

async def handle_conversation_message(db: Session, telegram_user_id: int, chat_id: int, text: str):
    session = TelegramSessionService.get_session(db, telegram_user_id)
    if session is None or session.current_state == "idle":
        return False

    state = session.current_state
    if state == "awaiting_registration_email":
        await process_registration_email(db, telegram_user_id, chat_id, text)

    elif state == "awaiting_login_email":
        await process_login_email(db, telegram_user_id, chat_id, text)

    elif state == "awaiting_login_pass_key":
        await process_login_pass_key(db, telegram_user_id, chat_id, text)
        
    else:
        await send_message(chat_id, "I couldn't identify your current conversation. Please try again.")
        TelegramSessionService.clear_session(db, telegram_user_id)
    return True