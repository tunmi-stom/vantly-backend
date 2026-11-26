from sqlalchemy import Column, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database.base import Base


class TelegramIdentity(Base):
    __tablename__ = "vantly_telegram_identities"

    id = Column(Integer, primary_key=True, index=True)
    telegram_user_id = Column(BigInteger, unique=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("vantly_users.id", ondelete="CASCADE"), unique=True, nullable=False)

    user = relationship("User")