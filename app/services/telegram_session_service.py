from sqlalchemy.orm import Session
from app.models.telegram_session import TelegramSession

class TelegramSessionService:
    @staticmethod
    def get_session(db: Session, telegram_user_id: int):
        return (
            db.query(TelegramSession).filter(
                TelegramSession.telegram_user_id == telegram_user_id
            ).first()
        )

    @staticmethod
    def set_state(
        db: Session,
        telegram_user_id: int,
        chat_id: int,
        state: str,
        temporary_data: dict | None = None
    ):
        session = TelegramSessionService.get_session(db, telegram_user_id)

        if session is None:
            session = TelegramSession(
                telegram_user_id=telegram_user_id,
                chat_id=chat_id,
                current_state=state,
                temporary_data=temporary_data
            )

            db.add(session)

        else:
            session.chat_id = chat_id
            session.current_state = state
            session.temporary_data = temporary_data

        db.commit()
        db.refresh(session)

        return session

    @staticmethod
    def update_data(
        db: Session,
        telegram_user_id: int,
        temporary_data: dict
    ):
        session = TelegramSessionService.get_session(db, telegram_user_id)
        if session is None:
            return None

        session.temporary_data = temporary_data

        db.commit()
        db.refresh(session)

        return session

    @staticmethod
    def clear_session(db: Session, telegram_user_id: int):
        session = TelegramSessionService.get_session(db, telegram_user_id)

        if session:
            session.current_state = "idle"
            session.temporary_data = None

            db.commit()

        return session