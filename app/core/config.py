from pydantic_settings import BaseSettings
from logging  import Logger, basicConfig, INFO, getLogger
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Settings(BaseSettings):
    # Project Information
    PROJECT_NAME: str = "Vantly"
    PROJECT_VERSION: str = "0.1.0"
    
    # API Settings
    API_V1_STR: str = "api/v1"
    
    # Database Settings
    DATABASE_URL: str = getenv("DATABASE_URL")
    
    # Security Settings
    JWT_SECRET: str = getenv("JWT_SECRET")
    JWT_ALGORITHM: str = getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_DELTA: str = getenv("ACCESS_TOKEN_EXPIRE_DELTA")
    
    # Telegram Bot Settings
    BOT_TOKEN: str = getenv("TG_BOT_TOKEN")
    BOT_WEBHOOK_URL: str = getenv("TG_BOT_WEBHOOK_URL")
    TELEGRAM_BOT_API: str = f"https://api.telegram.org/bot{BOT_TOKEN}"
    BOT_WEBHOOK_SECRET: str = getenv("WEBHOOK_SECRET")

settings = Settings()