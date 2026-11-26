from sqlalchemy import Column, Integer, BigInteger, String, DateTime, JSON
from sqlalchemy.sql import func
from app.core.database.base import Base


class TelegramSession(Base):
    __tablename__ = "vantly_telegram_sessions"

    id = Column(Integer, primary_key=True, index=True)
    telegram_user_id = Column(BigInteger, unique=True, nullable=False, index=True)
    chat_id = Column(BigInteger, nullable=False)
    current_state = Column(String, nullable=False, default="idle")
    temporary_data = Column(JSON, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())