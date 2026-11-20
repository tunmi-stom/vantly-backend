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

# For the /about keyboard
about_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Visit Documentations Page",
                callback_data="docs:url"
            )
        ]
    ]
)
# Convert topics keyboard to JSONdict
about_keyboard_payload = about_keyboard.to_dict()
