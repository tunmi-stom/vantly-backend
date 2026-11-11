from fastapi import HTTPException, status
from .handlers.start import handle_start
from .handlers.help import handle_help
from .handlers.send import handle_send

class Dispatcher:
    @staticmethod
    async def bot_start(chat_id: int, first_name: str):
        await handle_start(chat_id, first_name)
    
    @staticmethod
    async def bot_help(chat_id: int):
        await handle_help(chat_id)
        
    async def bot_send(chat_id: int, text: str):
        await handle_send(chat_id, text)
    
async def dispatch(update: dict):
    message = update.get("message")
    if message is None:
        return
    
    chat_id: int = message["chat"]["id"]
    text: str = message.get("text", "")
    first_name: str = message["from"].get("first_name")
    
    if text.startswith("/start"):
        await Dispatcher.bot_start(chat_id, first_name)
    
    elif text.startswith("/help"):
        await Dispatcher.bot_help(chat_id)
    
    else:
        await Dispatcher.bot_send(chat_id, text)