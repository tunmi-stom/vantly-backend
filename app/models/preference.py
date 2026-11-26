from sqlalchemy import String, Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database.base import Base
from app.utils.enums import RsdOps, EnableNotification, Language

class Preference(Base):
    __tablename__ = "vantly_user_preferences"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("vantly_users.id", ondelete="CASCADE"), unique=True, nullable=False)
    rsd_param = Column(String, default=RsdOps.CONCISE.value)
    enable_notification = Column(Boolean, default=EnableNotification.YES.value)
    language = Column(String, default=Language.ENG.value)
    
    # Relationship of User
    user = relationship("User", back_populates="preferences")