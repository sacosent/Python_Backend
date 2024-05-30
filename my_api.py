from fastapi import FastAPI
from typing import List
from user_db import User, user_list

app = FastAPI()

#--------------------- USER LOGIN ---------------------#

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/users", response_model=List[User])
def get_users():
    return user_list