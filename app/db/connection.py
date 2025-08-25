# import mysql.connector as msql
# import traceback


# def db_connection():
#     try:
#         print("trying to connect...")
#         mydb = msql.connect(
#             host="127.0.0.1",
#             port=3306,
#             user="root",
#             password="",
#             database="projectone"
#         )
#         print("Connected object:", mydb)
       
#         if mydb.is_connected():
#             print("Database connected successfully.")
#         else:
#             print("DB connection failed!")

#     except Exception as err:
#         print(f"Error: {err}")
#         traceback.print_exc()
#     finally:
#         if 'mydb' in locals() and mydb.is_connected():
#             mydb.close()
#             print("mysql connection is closed")


# if __name__ == "__main__":
#     db_connection()





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