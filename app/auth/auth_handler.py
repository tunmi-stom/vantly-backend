from fastapi import HTTPException, status
from datetime import datetime, timedelta, timezone
from jose import JWTError
from jose.jwt import encode, decode
from app.core.config import settings
from app.schemas.tokens import TokenData

def create_access_token(data: TokenData):
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_DELTA)
    
    payload = {
        "sub": data.id,
        "email": data.email,
        "iat": datetime.now(timezone.utc),
        "exp": expire,
        "subscription": data.subs
    }
    
    token = encode(payload, key=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    
    return token

def decode_jwt(token: str):
    try:
        payload = decode(token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token."
        )
        
    return payload