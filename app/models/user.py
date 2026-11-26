from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.core.database.base import Base
from app.utils.enums import Subs

class User(Base):
    __tablename__ = "vantly_users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    subscription = Column(String, default=Subs.FREE.value)
    
    # Relationship of Preference
    preferences = relationship("Preference", back_populates="user", uselist=False)