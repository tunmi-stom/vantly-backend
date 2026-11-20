from app.interfaces.telegram.client import send_message
from app.interfaces.telegram.keyboard.inline import about_keyboard_payload

async def handle_about(chat_id: int):
    message = (
        "About section in development.\n\n"
        "This is a work in progress.\n\n"
        "See /help for more information.\n\n"
    )
    await send_message(chat_id, message, about_keyboard_payload)