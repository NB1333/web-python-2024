from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .crud import create_user, get_user, get_users, update_user, delete_user
from .models import User
from .database import engine, SessionLocal

# Create a FastAPI instance
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new user
@app.post("/users/", response_model=User)
def create_user_route(username: str, email: str, db: Session = Depends(get_db)):
    return create_user(db, username=username, email=email)

# Endpoint to retrieve information about a user by ID
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id=user_id)

# Endpoint to retrieve a list of users with optional skip and limit parameters
@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

# Endpoint to update user information
@app.put("/users/{user_id}", response_model=User)
def update_user_route(user_id: int, username: str, email: str, db: Session = Depends(get_db)):
    return update_user(db, user_id=user_id, username=username, email=email)

# Endpoint to delete a user by ID
@app.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id=user_id)
    return {"message": f"User {user_id} deleted"}
