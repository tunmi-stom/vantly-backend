from app.interfaces.telegram.client import send_message
from app.interfaces.telegram.keyboard.inline import start_keyboard_payload

async def handle_start(chat_id: int, first_name: str):
    message = (
        f"Welcome to Vantly, {first_name}!\n\n"
        "This is a work in progress.\n\n"
        "Follow the development:\n"
        "https://github.com/tunmi-stom/vantly-backend\n\n"
        "See /help for more information.\n\n"
        "Thank you!\n\n"
        "Click Register below to create your account.\n"
    )
    await send_message(chat_id, message, start_keyboard_payload)

# Handle email input
async def handle_email_registration(chat_id: int):
    pass