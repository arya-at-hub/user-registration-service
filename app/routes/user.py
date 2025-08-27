from fastapi import APIRouter
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserSignup, UserLogin, UserUpdate, PasswordOTP, PAsswordReset
from app.functions.db import get_db
from app.functions.auth_utils import hash_password, verify_password, create_access_token, get_current_user
from app.functions.email_utils import send_email
from app.functions.otp_utils import generate_otp
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.otp import OTP
from datetime import datetime, timedelta

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_data():
    return {"message": "hello fastapi"}



@router.post("/forgot_password/{email_id}")
async def forget_password(email_id: str, db: Session = Depends(get_db)):
    
    user = db.query(User).filter(
        (User.email == email_id)).first()
    
    if not user:
        return {"message":"User does not exist!"}
    
    otp_entry = db.query(OTP).filter(OTP.email == email_id).first()
    otp = generate_otp()

    if otp_entry:
        otp_entry.otp = otp
        otp_entry.expires_at = datetime.now() + timedelta(minutes=10)
    else:
        otp_entry = OTP(
        email = email_id,
        otp = otp,
        expires_at = datetime.now() + timedelta(minutes=10))
        db.add(otp_entry)

    
    # print("otp:",otp)
    
    db.commit()
    db.refresh(otp_entry)
    await send_email(email_id, otp)
    
    return {"message": "OTP sent"}




@router.post("/verify_otp")
async def verify_otp(otp_data: PasswordOTP, db: Session = Depends(get_db)):
    otp_user = db.query(OTP).filter(
        OTP.email == otp_data.email,
        OTP.otp == otp_data.otp).first()
    
    if not otp_user:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if datetime.now() > otp_user.expires_at:
        raise HTTPException(status_code=400, detail="OTP expired")

    db.delete(otp_user)
    db.commit()
    return {"status_code":200, "message": "OTP verified, proceed to reset password"}



@router.post("/reset_password")
async def reset_password(user_data:PAsswordReset, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found!")
    hashed_pwd = hash_password(user_data.password)
    user.password = hashed_pwd
    db.commit()
    
    return {"status_code":200, "message": "Password reset successful"}
