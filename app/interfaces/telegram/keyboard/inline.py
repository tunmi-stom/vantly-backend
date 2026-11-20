from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton
)

# For the /start command
start_keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Create an Account",
                callback_data="start:register"
            ),
            InlineKeyboardButton(
                "Account Login",
                callback_data="start:login"
            )
        ]   
    ]
)
# Convert to JSONDict for Telegram's API
start_keyboard_payload = start_keyboard.to_dict()