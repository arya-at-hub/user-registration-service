# FastAPI User Service 
A simple microservice for **user authentication, registration, and profile management** using:  
- **FastAPI** (for APIs)  
- **SQLAlchemy** (for database handling)  
- **JWT** (for secure authentication)  
- **Pydantic** (for validation)  

# Features
- User Registration
- User Login with JWT authentication
- Secure Password Hashing
- Profile Update (with validation)



# To Activate the Virtual Environment
Run Command
- .venv\Scripts\activate  


# To install all the dependencies: 
Run Command
- pip install -r requirements.txt


# To Create Tables 
Run Command
- python -m app.db.create_tables


# To run the Project
Run Command
- uvicorn app.main:app --reload
