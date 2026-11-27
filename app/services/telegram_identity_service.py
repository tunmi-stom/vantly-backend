from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.telegram_identity import TelegramIdentity

class TelegramIdentityService:
    @staticmethod
    def get_identity(db: Session, telegram_user_id: int):
        return (
            db.query(TelegramIdentity).filter(
                TelegramIdentity.telegram_user_id == telegram_user_id
            ).first()
        )

    @staticmethod
    def link_identity(
        db: Session,
        telegram_user_id: int,
        user_id: int
    ):
        existing_telegram = TelegramIdentityService.get_identity(db, telegram_user_id)

        if existing_telegram:
            if existing_telegram.user_id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="This Telegram account is already linked."
                )

            return existing_telegram

        existing_user = (
            db.query(TelegramIdentity).filter(TelegramIdentity.user_id == user_id).first()
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This Vantly account is already linked to another Telegram account."
            )

        identity = TelegramIdentity(
            telegram_user_id=telegram_user_id,
            user_id=user_id
        )

        try:
            db.add(identity)
            db.commit()
            db.refresh(identity)

        except IntegrityError:
            db.rollback()

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Unable to link Telegram account."
            )

        return identity