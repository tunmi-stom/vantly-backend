from app.interfaces.telegram.client import send_message

async def handle_settings(chat_id: int):
    message = (
        "Settings in development.\n"
        "This is a work in progress.\n"
        "See /help for more information.\n"
    )
    await send_message(chat_id, message)