from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional




class UserInfo(BaseModel):
    email: EmailStr
    password: str    

class UserRegister(UserInfo):
    pass

class UserLogin(UserInfo):
    pass

class BaseToken(BaseModel):
    token: str

class BaseMessage(BaseModel):
    message: str    