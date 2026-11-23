from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton
)

# For the /start keyboard
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

# RSD Keyboard
rsd_keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "Consise",
            callback_data="rsd:consise"
        ),
        InlineKeyboardButton(
            "Standard",
            callback_data="rsd:standard"
        ),
        InlineKeyboardButton(
            "Detailed",
            callback_data="rsd:detailed"
        )
    ]
])
# Convert Keyboard to JSONDict
rsd_keyboard_payload = rsd_keyboard.to_json()

# Language Keyboard
lang_keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "English",
            callback_data="lang:en"
        )
    ]
])
# Convert Keyboard to JSONDict
lang_keyboard_payload = lang_keyboard.to_json()

# Notification Keyboard
notification_keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "Enable",
            callback_data="notifications:enable"
        ),
        InlineKeyboardButton(
            "Disable",
            callback_data="notifications:disable"
        )
    ]
])
# Convert Keyboard to JSONDict
notification_keyboard_payload = notification_keyboard.to_json()
