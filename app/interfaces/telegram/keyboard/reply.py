from telegram import KeyboardButton, ReplyKeyboardMarkup

# For the /start command
start_keyboard = ReplyKeyboardMarkup([
        [
            KeyboardButton(
            "Research a Topic"
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
start_keyboard_payload = start_keyboard.to_dict()

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
