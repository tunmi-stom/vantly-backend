from app.interfaces.telegram.client import send_message

async def handle_topics(chat_id: int):
    message = (
        "Topics section in development.\n\n"
        "This is a work in progress.\n\n"
        "See /help for more information.\n\n"
    )
    await send_message(chat_id, message)