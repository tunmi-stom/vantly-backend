from app.interfaces.telegram.client import send_message

async def handle_help(chat_id: int):
    message = (
        "Help Unavailable for now.\n\n"
        "Follow the development:\n"
        "1. Head over to https://github.com/tunmi-stom/vantly-backend\n\n"
        "2. And Star the Repository.\n"
        "3. Then, Check back for updates!"
    )
    await send_message(chat_id, message)