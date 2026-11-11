from app.interfaces.telegram.client import send_message

async def handle_send(chat_id: int, text: str):
    message = (
        "What would you have me do?\n"
        f"You sent: {text}"
    )
    await send_message(chat_id, message)