from pydantic import BaseModel, EmailStr, constr
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    admin = "admin"
    staff = "staff"
    student = "student"

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole = UserRole.student

# Registration Input
class UserCreate(UserBase):
    password: str = constr(min_length=6)

# Login Input
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Output schema
class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
