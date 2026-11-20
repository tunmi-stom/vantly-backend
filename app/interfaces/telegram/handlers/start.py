from app.interfaces.telegram.client import send_message

async def handle_start(chat_id: int, first_name: str):
    message = (
        f"Welcome to Vantly, {first_name}!\n\n"
        "This is a work in progress.\n\n"
        "Follow the development:\n"
        "https://github.com/tunmi-stom/vantly-backend\n\n"
        "See /help for more information.\n\n"
        "Thank you!"
    )
    await send_message(chat_id, message)