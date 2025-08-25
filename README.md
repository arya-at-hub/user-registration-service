# FastAPI User Service 
A microservice for user authentication, registration, and profile updates using FastAPI, SQLAlchemy, JWT, and Pydantic.

## Features
- User Registration
- User Login with JWT
- Profile Update
- Secure Password Hashing



# To Activate the Virtual Environment
- .venv\Scripts\activate  


# To install all the dependencies: 
Run Command
- pip install -r requirements.txt


# To Create Tables 
Run Command
- python -m app.db.create_tables


# To run the Project
- uvicorn app.main:app --reload