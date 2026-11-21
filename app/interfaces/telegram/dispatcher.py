from .handlers.start import handle_start, handle_email_registration, handle_email_login
from .handlers.help import handle_help
from .handlers.send import handle_send
from .handlers.topics import handle_topics
from .handlers.research import handle_research
from .handlers.settings import handle_settings
from .handlers.about import handle_about
# Handling testing
from .client import edit_message

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
    async def bot_send(chat_id: int, text: str):
        await handle_send(chat_id, text)
class ChatHandler:
    @staticmethod
    async def message_handler(update: dict):
        msg = update.get("message")
        
        chat_id: int = msg["chat"]["id"]
        text: str = msg.get("text", "")
        first_name: str = msg["from"].get("first_name")
        
        if text == "/start":
            await Dispatcher.bot_start(chat_id, first_name)
        
        elif text == "/help" or text == "Help":
            await Dispatcher.bot_help(chat_id)
        
        elif text == "/about" or text == "More Info":
            await Dispatcher.bot_about(chat_id)
        
        elif text == "/settings" or text == "Preferences":
            await Dispatcher.bot_settings(chat_id)
        
        elif text == "/topics":
            await Dispatcher.bot_topics(chat_id)
        
        elif text == "/research":
            await Dispatcher.bot_research(chat_id)
        
        else:
            await Dispatcher.bot_send(chat_id, text)
    
    @staticmethod
    async def callback_handler(update: dict):
        data: dict = update.get("callback_query")
        
        # Isolate the callback_data
        callback_data: str = data.get("data")
        
        msg: dict = data.get("message")
        
        # Get the params from the message
        msg_id = msg.get("message_id")
        chat_id: str = msg["chat"]["id"]
        
        match callback_data:
            case "start:register":
                await handle_email_registration(chat_id, msg_id)
                
            case "start:login":
                await handle_email_login(chat_id, msg_id)
                
async def dispatch(update: dict):
    if "message" in update:
        await ChatHandler.message_handler(update)
    elif "callback_query" in update:
        await ChatHandler.callback_handler(update)