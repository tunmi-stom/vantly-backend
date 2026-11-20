from telegram import KeyboardButton, ReplyKeyboardMarkup

# For registered users
user_start_keyboard = ReplyKeyboardMarkup([
        [
            KeyboardButton(
            "Research a Topic"
            ),
            KeyboardButton(
                "Join Beta"
            )
        ],
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
    ], resize_keyboard=True
)
# Convert to JSONDict for Telegram's API
user_start_keyboard_payload = user_start_keyboard.to_dict()

# For the /topics keyboard
topic_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                "Manage Topics"
            )
        ]
    ], resize_keyboard=True
)
# Convert topics keyboard to JSONdict
topic_keyboard_payload = topic_keyboard.to_dict()

# For the /about keyboard
about_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                "Visit Documentations Page"
            )
        ]
    ], resize_keyboard=True
)
# Convert topics keyboard to JSONdict
about_keyboard_payload = about_keyboard.to_dict()