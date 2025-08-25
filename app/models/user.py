from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from app.db.connection import Base
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(13), nullable=True)
    gender = Column(String(10), nullable=True)
    address = Column(String(255), nullable=True)
    dob = Column(Date, nullable=True)
    profile_photo = Column(String(255), nullable=True)

    role = Column(String(50), default="user")
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
