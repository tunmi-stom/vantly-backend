from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery
)

# For the /start command
start_keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Create an Account",
                callback_data=CallbackQuery("start:register")
            ),
            InlineKeyboardButton(
                "Account Login",
                callback_data=CallbackQuery("start:login")
            )
        ]   
    ], resize_keyboard=True
)
# Convert to JSONDict for Telegram's API
start_keyboard_payload = start_keyboard.to_dict()