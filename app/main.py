from fastapi import FastAPI
from app.db.connection import db_connection, Base, engine
from app.routes import user, auth
from app.models import user as user_models, otp as otp_models
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_connection()
    yield


app = FastAPI(lifespan=lifespan)

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Welcome to my Project!"}