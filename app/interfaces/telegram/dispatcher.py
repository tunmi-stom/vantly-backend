from .handlers.start import (
    handle_start,
    handle_email_registration,
    handle_email_login
)
from .handlers.help import handle_help
from .handlers.send import handle_send
from .handlers.topics import handle_topics
from .handlers.research import handle_research
from .handlers.settings import (
    handle_settings,
    handle_research_summary_depth_settings,
    handle_language_settings,
    handle_notifictation_settings
)
from .handlers.about import handle_about

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

class ChatHandler:

    @staticmethod
    async def message_handler(update: dict):

        msg = update.get("message")

        if not isinstance(msg, dict):
            logger.warning("Invalid message update received.")
            return

        chat = msg.get("chat")
        user = msg.get("from")

        if not isinstance(chat, dict) or "id" not in chat:
            logger.warning("Message update has no valid chat information.")
            return

        chat_id = chat["id"]

        first_name = (
            user.get("first_name", "there")
            if isinstance(user, dict)
            else "there"
        )

        # Handle text messages.
        if "text" in msg:

            text = msg["text"]

            if not isinstance(text, str):
                logger.warning("Invalid text message received.")
                return

            if text == "/start":
                await Dispatcher.bot_start(chat_id, first_name)

            elif text in ("/help", "Help"):
                await Dispatcher.bot_help(chat_id)

            elif text in ("/about", "More Info"):
                await Dispatcher.bot_about(chat_id)

            elif text in ("/settings", "Preferences"):
                await Dispatcher.bot_settings(chat_id)

            elif text == "/topics":
                await Dispatcher.bot_topics(chat_id)

            elif text == "/research":
                await Dispatcher.bot_research(chat_id)

            else:
                await Dispatcher.bot_send(chat_id, text)

        # Handle unsupported message types.
        elif "voice" in msg:
            await send_message(chat_id, "Voice messages are not supported yet. Please send a text message.")
        
        elif "document" in msg:
            await send_message(chat_id, "Document processing is not available yet.")

        elif "photo" in msg:
            await send_message(chat_id, "Image processing is not available yet.")

        elif "sticker" in msg:
            await send_message(chat_id, "Please send your message as text.")

        else:
            logger.info("Received an unsupported message type.")


    @staticmethod
    async def callback_handler(update: dict):

        data = update.get("callback_query")

        if not isinstance(data, dict):
            logger.warning("Invalid callback query received.")
            return

        callback_query_id = data.get("id")
        callback_data = data.get("data")

        msg = data.get("message")

        # Acknowledge the callback to stop Telegram's loading indicator.
        if callback_query_id:
            await answer_callback_query(callback_query_id)

        # Inline callbacks may not contain a normal message.
        if not isinstance(msg, dict):
            logger.info("Callback query has no associated message.")
            return

        chat = msg.get("chat")

        if not isinstance(chat, dict) or "id" not in chat:
            logger.warning("Callback query has no valid chat information.")
            return

        chat_id = chat["id"]
        msg_id = msg.get("message_id")

        if not isinstance(callback_data, str):
            logger.warning("Callback query has invalid callback data.")
            return

        match callback_data:

            case "start:register":
                await handle_email_registration(chat_id, msg_id)

            case "start:login":
                await handle_email_login(chat_id, msg_id)

            case "settings:research-summary-depth":
                await handle_research_summary_depth_settings(chat_id, msg_id)

            case "settings:notifications":
                await handle_notifictation_settings(chat_id, msg_id)

            case "settings:language":
                await handle_language_settings(chat_id, msg_id)

            case _:
                logger.warning(
                    "Unknown callback data received: %s",
                    callback_data
                )

                await send_message(chat_id, "This action is not recognised. Please try again.")


async def dispatch(update: dict):

    if not isinstance(update, dict):
        logger.warning("Invalid Telegram update received.")
        return

    try:

        if "message" in update:
            await ChatHandler.message_handler(update)

        elif "callback_query" in update:
            await ChatHandler.callback_handler(update)

        else:
            logger.info(
                "Unsupported Telegram update type. Update ID: %s",
                update.get("update_id")
            )

    except Exception:
        logger.exception(
            "Unexpected error while dispatching Telegram update. "
            "Update ID: %s",
            update.get("update_id")
        )
        raise