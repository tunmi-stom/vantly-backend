from app.interfaces.telegram.client import send_message
from app.interfaces.telegram.keyboard.inline import settings_keyboard_payload

async def handle_settings(chat_id: int):
    message = (
        "User Settings.\n"
        "This is a work in progress.\n"
        "See /help for more information.\n"
    )
    await send_message(chat_id, message, settings_keyboard_payload)