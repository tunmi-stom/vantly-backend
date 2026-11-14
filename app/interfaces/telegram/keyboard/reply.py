from telegram import KeyboardButton, ReplyKeyboardMarkup

# For the /start command
start_keyboard = ReplyKeyboardMarkup([
    KeyboardButton(
        "Research a Topic"
    ),
    [
        KeyboardButton(
            "Preferences"
        ),
        KeyboardButton(
            "More Info"
        ),
        KeyboardButton(
            "Help"
        )
    ]
])

start_keyboard_payload = start_keyboard.to_dict()