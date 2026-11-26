from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.interfaces.telegram.client import send_message, edit_message
from app.interfaces.telegram.keyboard.inline import start_keyboard_payload
from app.services.user_services import UserService
from app.utils.helpers import generate_random_key, check_email_str
from app.schemas.users import UserSignupData, UserLoginData
from app.services.telegram_identity_service import TelegramIdentityService
from app.services.telegram_session_service import TelegramSessionService
from app.models.user import User

async def handle_start(chat_id: int, first_name: str):
    message = (
        f"Welcome to Vantly, {first_name}!\n\n"
        "This is a work in progress.\n\n"
        "Follow the development:\n"
        "https://github.com/tunmi-stom/vantly-backend\n\n"
        "See /help for more information.\n\n"
        "Thank you!\n\n"
        "Click Register below to create your account.\n"
    )
    await send_message(chat_id, message, start_keyboard_payload)

# REGISTER: INITIAL STEP
async def handle_email_registration(
    db: Session,
    telegram_user_id: int,
    chat_id: int
):
    existing_identity = TelegramIdentityService.get_identity(db, telegram_user_id)
    if existing_identity:
        await send_message(chat_id, "You already have a Vantly account linked to this Telegram account.")
        return

    TelegramSessionService.set_state(
        db=db,
        telegram_user_id=telegram_user_id,
        chat_id=chat_id,
        state="awaiting_registration_email"
    )

    await send_message(
        chat_id,
        "Let's create your Vantly account.\n\n"
        "Please enter your email address."
    )
    


# LOGIN: INITIAL STEP
async def handle_email_login(
    db: Session,
    telegram_user_id: int,
    chat_id: int
):
    existing_identity = TelegramIdentityService.get_identity(db, telegram_user_id)
    if existing_identity:
        await send_message(chat_id, "You're already connected to your Vantly account.")
        return

    TelegramSessionService.set_state(
        db=db,
        telegram_user_id=telegram_user_id,
        chat_id=chat_id,
        state="awaiting_login_email"
    )
    
    init_login_message = (
        "Welcome back!\n\n"
        "Please enter your Vantly account email."
    )
    await send_message(chat_id, init_login_message)

# PROCESS REGISTRATION EMAIL
async def process_registration_email(
    db: Session,
    telegram_user_id: int,
    chat_id: int,
    email: str
):
    email = email.strip().lower()
    if not check_email_str(email):
        await send_message(
            chat_id, "Please enter a valid email address.")
        return

    pass_key = generate_random_key()
    try:
        UserService.create_user(db, UserSignupData(email=email, password=pass_key))
        user = db.query(User).filter(User.email == email).first()

        if user is None:
            raise RuntimeError("Created user could not be retrieved.")

        TelegramIdentityService.link_identity(db, telegram_user_id, user.id)

    except HTTPException as exc:
        await send_message(chat_id, f"Registration failed: {exc.detail}")
        return

    except Exception:
        await send_message(chat_id, "Something went wrong during registration. Please try again.")
        return

    TelegramSessionService.clear_session(db, telegram_user_id)
    await send_message(
        chat_id,
        "Registration successful!\n\n"
        "Your Vantly account has been created.\n\n"
        f"Your pass_key is:\n`{pass_key}`\n\n"
        "Keep this key safe. You will need it when accessing "
        "your account through another interface.\n\n"
        "Welcome to Vantly!"
    )


# PROCESS LOGIN EMAIL
async def process_login_email(
    db: Session,
    telegram_user_id: int,
    chat_id: int,
    email: str
):
    email = email.strip().lower()

    if not check_email_str(email):
        await send_message(chat_id, "Invalid email address. Please try again.")
        return

    TelegramSessionService.set_state(
        db=db,
        telegram_user_id=telegram_user_id,
        chat_id=chat_id,
        state="awaiting_login_pass_key",
        temporary_data={"email": email}
    )

    await send_message(chat_id, "Email received.\n\n" "Now enter your pass_key.")

# PROCESS LOGIN PASS_KEY
async def process_login_pass_key(
    db: Session,
    telegram_user_id: int,
    chat_id: int,
    pass_key: str
):
    session = TelegramSessionService.get_session(db, telegram_user_id)
    if not session or not session.temporary_data:
        await send_message(chat_id, "Your login session has expired. Please start again.")
        TelegramSessionService.clear_session(db, telegram_user_id)
        return

    email = session.temporary_data.get("email")
    try:
        login_response = UserService.login_telegram_user(db, UserLoginData(email=email, password=pass_key))

        user_data = login_response["data"]
        TelegramIdentityService.link_identity(
            db,
            telegram_user_id,
            user_data["id"]
        )

    except HTTPException:
        await send_message(chat_id, "Login failed. Please check your email and pass_key.")
        return

    except Exception:
        await send_message(chat_id, "An unexpected error occurred during login.")
        return

    TelegramSessionService.clear_session(db, telegram_user_id)

    await send_message(
        chat_id,
        "Login successful!\n\n"
        f"Welcome back, {email}.\n\n"
        "Your Vantly account is now connected to Telegram."
    )