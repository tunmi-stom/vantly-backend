from .handlers.start import handle_start
from .handlers.help import handle_help
from .handlers.send import handle_send
from .handlers.topics import handle_topics
from .handlers.research import handle_research
from .handlers.settings import handle_settings
from .handlers.about import handle_about

class Dispatcher:
    @staticmethod
    async def bot_start(chat_id: int, first_name: str):
        await handle_start(chat_id, first_name)
    
    @staticmethod
    async def bot_help(chat_id: int):
        await handle_help(chat_id)
        
    @staticmethod
    async def bot_about(chat_id: int):
        await handle_about(chat_id)
    
    @staticmethod
    async def bot_settings(chat_id: int):
        await handle_settings(chat_id)
    
    @staticmethod
    async def bot_topics(chat_id: int):
        await handle_topics(chat_id)
    
    @staticmethod
    async def bot_research(chat_id: int):
        await handle_research(chat_id)
    
    @staticmethod
    async def bot_send(chat_id: int):
        await handle_send(chat_id)
class ChatHandler:
    @staticmethod
    async def message_handler(data: dict):
        msg = data.get("message")
        
        chat_id: int = msg["chat"]["id"]
        text: str = msg.get("text", "")
        first_name: str = msg["from"].get("first_name")
        
        if text.startswith("/start"):
            await Dispatcher.bot_start(chat_id, first_name)
        
        elif text.startswith("/help"):
            await Dispatcher.bot_help(chat_id)
        
        elif text.startswith("/about"):
            await Dispatcher.bot_about(chat_id)
        
        elif text.startswith("/settings"):
            await Dispatcher.bot_settings(chat_id)
        
        elif text.startswith("/topics"):
            await Dispatcher.bot_topics(chat_id)
        
        elif text.startswith("/research"):
            await Dispatcher.bot_research(chat_id)
        
        else:
            await Dispatcher.bot_send(chat_id)
    
    @staticmethod
    async def callback_handler(data: dict):
        callback_data = data.get("data")
        match callback_data:
            case "settings:setalias":
                pass
            case "settings:subscription":
                pass
            
async def dispatch(update: dict):
    if "message" in update:
        await ChatHandler.message_handler(update)
    elif "callback_query" in update:
        await ChatHandler.callback_handler(update)