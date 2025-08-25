from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_data():
    return {"msg":"hello fastapi"}


@router.post("/")
def create_user():
    return {"message": "User created"}