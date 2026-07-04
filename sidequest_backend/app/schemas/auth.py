from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional, Literal

Role = Literal["user", "moderator", "admin"]

class UserBase(BaseModel):
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class UserPublic(UserBase):
    id: int
    role: Role
    is_active: bool

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str= Field(min_length=6, max_length=70)
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type: str = "bearer"
    user: UserPublic

class TokenData(BaseModel):
    sub: str
    username: str

class RoleUpdate(BaseModel):
    role: Role
