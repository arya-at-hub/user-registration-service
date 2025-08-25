from app.db.connection import Base, engine
from app.models.user import User 

def create_all_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_all_tables()

