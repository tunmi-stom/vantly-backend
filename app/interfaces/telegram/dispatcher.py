from sqlalchemy.orm import Session
from .handlers.help import handle_help
from .handlers.send import handle_send
from .handlers.topics import handle_topics
from .handlers.research import handle_research
from .handlers.about import handle_about
from .handlers.conversation import handle_conversation_message
from .handlers.start import (
    handle_start,
    handle_email_registration,
    handle_email_login
)
from .handlers.settings import (
    handle_settings,
    handle_research_summary_depth_settings,
    handle_language_settings,
    handle_notifictation_settings
)
from app.core.database.dependency import db_dependency

from .client import send_message, answer_callback_query
from app.core.logging import logger


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

    @staticmethod
    async def bot_register(db: Session, telegram_user_id: int, chat_id: int):
        await handle_email_registration(db, telegram_user_id, chat_id)

    @staticmethod
    async def bot_login(db: Session, telegram_user_id: int, chat_id: int):
        await handle_email_login(db, telegram_user_id, chat_id)

    @staticmethod
    async def bot_conversation(db: Session, telegram_user_id: int, chat_id: int, text: str):
        return await handle_conversation_message(db, telegram_user_id, chat_id, text)

class ChatHandler:

    @staticmethod
    async def message_handler(db: Session, update: dict):
        msg = update.get("message")
        if not msg:
            return

        chat_id = msg["chat"]["id"]
        telegram_user_id = msg["from"]["id"]
        text = msg.get("text", "").strip()
        first_name = msg["from"].get("first_name", "there")

        if text.startswith("/start"):
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
            handled = await Dispatcher.bot_conversation(db, telegram_user_id, chat_id, text)

            if not handled:
                await Dispatcher.bot_send(chat_id, text)

    @staticmethod
    async def callback_handler(db: Session, update: dict):
        data = update.get("callback_query")
        if not data:
            return

        callback_data = data.get("data")

        msg = data.get("message")
        if not msg:
            return
        
        msg_id = msg.get("message_id")
        chat_id = msg["chat"]["id"]
        telegram_user_id = data["from"]["id"]

        match callback_data:

            case "start:register":
                await Dispatcher.bot_register(db, telegram_user_id, chat_id)

            case "start:login":
                await Dispatcher.bot_login(db, telegram_user_id, chat_id)

            case "settings:research-summary-depth":
                await handle_research_summary_depth_settings(chat_id, msg_id)

            case "settings:notifications":
                await handle_notifictation_settings(chat_id, msg_id)

            case "settings:language":
                await handle_language_settings(chat_id, msg_id)

async def dispatch(db: db_dependency, update: dict):
    if "message" in update:
        await ChatHandler.message_handler(db, update)
    elif "callback_query" in update:
        await ChatHandler.callback_handler(db, update)
