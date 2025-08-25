from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional
from datetime import date

class UserSignup(BaseModel):
    username: str
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    profile_photo: Optional[str] = None
    role: Optional[str] = "user"

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: str

    @model_validator(mode="after")
    def check_email_or_username(self):
        if not self.email and not self.username:
            raise ValueError("Either email or username must be provided.")
        return self


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    profile_photo: Optional[str] = None