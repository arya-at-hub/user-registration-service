from fastapi import FastAPI
from app.db.connection import db_connection
from app.routes import user, auth
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_connection()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Welcome to my Project!"}