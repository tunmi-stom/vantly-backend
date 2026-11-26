from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.users import UserSignupData, UserResponse, UserLoginData
from app.schemas.tokens import TokenData
from app.models.user import User
from app.models.preference import Preference
from app.utils.helpers import hash_password, verify_password
from app.core.logging import logger
from app.auth.auth_handler import create_access_token

class UserService:
    @staticmethod
    def create_user(db: Session, create_user_data: UserSignupData):
        # Normalise EmailStr
        user_email = create_user_data.email.strip().lower()
        
        # Check if user exists
        db_user = db.query(User).filter(User.email == user_email).first()
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already Exists."
            )
            
        # Create a user
        new_user = User(
            email=user_email,
            hashed_password=hash_password(create_user_data.password)
        )
        
        try:
            user_preference = Preference(user=new_user)
            
            db.add(new_user)
            db.add(user_preference)
            
            db.commit()
        except IntegrityError as err:
            db.rollback()
            logger.exception("Database Integrity Error: %s", err)
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Database Integrity Error."
            )
        except Exception as e:
            db.rollback()
            logger.exception("A Database error occured while adding user. Error: %s", e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="A Database error occured while adding user."
            )
            
        return UserResponse.model_validate(new_user)
    
    @staticmethod
    def login_telegram_user(db: Session, data: UserLoginData):
        # Normalise the email
        email = data.email.strip().lower()
        
        # Check if user exists
        user = db.query(User).filter(User.email == email).first()
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )
            
        if not verify_password(data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect Password."
            )
        
        user_data = {
            "id": user.id,
            "email": user.email,
            "subscription": user.subscription,
            "preferences": {
                "user_id": user.preferences.user_id,
                "rsd_param": user.preferences.rsd_param,
                "enable_notification": user.preferences.enable_notification,
                "language": user.preferences.language
            }
        }
        
        return {
            "data": user_data
        }
    
    @staticmethod
    def login_user(db: Session, login_data: UserLoginData):
        # Normalise the email
        email = login_data.email.strip().lower()
        
        # Check if user exists
        user = db.query(User).filter(User.email == email).first()
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )
        
        if not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect Password."
            )
        
        data = TokenData(email=email, id=user.id, subs=user.subscription)
        token = create_access_token(data)
        
        return {
            "access_token": token,
            "token_type": "bearer"
        }