from app.interfaces.telegram.client import send_message, edit_message
from app.interfaces.telegram.keyboard.inline import (
    settings_keyboard_payload, rsd_keyboard_payload,
    notification_keyboard_payload, lang_keyboard_payload
)

async def handle_settings(chat_id: int):
    message = (
        "Settings in development.\n"
        "This is a work in progress.\n"
        "See /help for more information.\n"
    )
    await send_message(chat_id, message, settings_keyboard_payload)

# Handler Function for Research Summary Depth
async def handle_research_summary_depth_settings(chat_id: int, msg_id: int):
    message = (
        "Choose Research Summary Depth:"
    )
    
    await edit_message(chat_id, message, msg_id, rsd_keyboard_payload)

# Handler Function for Notifications
async def handle_notifictation_settings(chat_id: int, msg_id: int):
    message = (
        "Choose Notification Style:"
    )
    
    await edit_message(chat_id, message, msg_id, notification_keyboard_payload)

# Handler Function for Language
async def handle_language_settings(chat_id: int, msg_id: int):
    message = (
        "Choose Preferred Language:"
    )
    
    await edit_message(chat_id, message, msg_id, lang_keyboard_payload)