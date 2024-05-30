from fastapi import FastAPI
from typing import List
from user_db import User, users

app = FastAPI()

@app.get("/users", response_model=List[User])
def get_users():
    return users
