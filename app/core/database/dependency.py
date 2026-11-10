from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from .db_config import get_db, engine, Base

db_dependency = Annotated[Session, Depends(get_db)]

def init_db():
    Base.metadata.create_all(bind=engine)