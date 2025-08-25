from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserSignup, UserLogin, UserUpdate
from app.functions.db import get_db
from app.functions.auth import hash_password, verify_password, create_access_token, get_current_user
from sqlalchemy.orm import Session
from app.models.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/signup")
def signup(user_data: UserSignup, db: Session = Depends(get_db)):

    hashed_pwd = hash_password(user_data.password)

    existing_user = db.query(User).filter(
        (User.username == user_data.username) | 
        (User.email == user_data.email)).first()
    
    if existing_user:
        return {"message":"Username or Email already exists!"}
    
    user_dict = user_data.model_dump()
    user_dict['password'] = hashed_pwd

    new_user = User(**user_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": f"Welcome {user_data.username}"}
    

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    
    user = db.query(User).filter(
        ((User.username == user_data.username) |
        (User.email == user_data.email))).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    if not verify_password(user_data.password, user.password):
         raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    token = create_access_token({"sub": str(user.id)})
    return {"message": f"User {user_data.email} logged in successfully.",
            "access_token": token,
            "token_type": "bearer"}



@router.patch("/user_data_update/{user_id}")
def user_update(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    existing_user = db.query(User).filter(
        (User.id == user_id)).first()
    
    if not existing_user:
        return {"message":"User does not exist!"}
    
    user_dict = user_data.model_dump(exclude_unset=True)
    
    for key, value in user_dict.items():
        setattr(existing_user, key, value)
    
    db.commit()
    db.refresh(existing_user)
    
    return {"message": "Details Updated",
            "details": existing_user}
