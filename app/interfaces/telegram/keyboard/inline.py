from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton
)

# For the /start command
start_keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Register",
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
                url="https://github.com/tunmi-stom/vantly-backend/blob/main/README.md"
            )
        ]
    ]
)
# Convert topics keyboard to JSONdict
about_keyboard_payload = about_keyboard.to_dict()

# Keyboard for the /settings command
settings_keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "Research Summary Depth",
            callback_data="settings:research-summary-depth"
        )
    ],
    [
        InlineKeyboardButton(
            "Report Presentation",
            callback_data="settings:research-presentation"
        )
    ],
    [
        InlineKeyboardButton(
            "Language",
            callback_data="settings:language"
        )
    ],
    [
        InlineKeyboardButton(
            "Notifications",
            callback_data="settings:notifications"
        )
    ]
])
# Convert settings keyboard to JSONdict
settings_keyboard_payload = settings_keyboard.to_json()