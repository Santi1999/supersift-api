from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class ResultsBase(BaseModel):
    title: str
    url: str
    content: str


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str

class UserOut(BaseModel):
    id : int
    email: EmailStr
    created_at: datetime

    class congfig:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None