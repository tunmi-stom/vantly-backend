from pydantic import BaseModel, ConfigDict, EmailStr

class UserSchema(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    hashed_password: str
    subscription: str
    
class UserLoginData(BaseModel):
    email: EmailStr
    password: str
    
class UserSignupData(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)