from app.interfaces.telegram.client import send_message

async def handle_help(chat_id: int):
    message = (
        "Bot Commands and Usage.\n\n"
        "List of Vantly's Commands:\n"
        "1. /start - Start the bot.\n"
        "2. /help - Command discovery and Bot Manual.\n"
        "3. /about - Product information.\n"
        "4. /settings - User preferences.\n"
        "5. /topics - Topic management.\n"
        "6. /research - Research management.\n\n"
    )
    await send_message(chat_id, message)