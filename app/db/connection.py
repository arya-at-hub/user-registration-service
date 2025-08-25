from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def db_connection():
    try:
        conn = engine.connect()
        print("DB connected successfully.")
        return conn

    except SQLAlchemyError as e:
        print("DB connection failed:",e)


Base = declarative_base()