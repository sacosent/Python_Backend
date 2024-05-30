from fastapi import FastAPI, HTTPException, Query, Body
from typing import List, Optional
from user_db import User, user_list, user_filter

app = FastAPI()

#--------------------- USER LOGIN ---------------------#

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/users", response_model=List[User])
async def users():
    return user_list

@app.get("/users/listfilter", response_model=List[User])
def get_users_by_ids(user_ids: List[int] = Query(...)):
    
    filtered_users = user_filter(filter_type="list", user_ids=user_ids)
    return filtered_users

@app.get("/users/rangefilter", response_model=List[User])
def get_users_by_range(start_id: int, end_id: int):
    
    filtered_users = user_filter(filter_type="range", start_id=start_id, end_id=end_id)
    return filtered_users

# Endpoint to add new users to the user_db file
@app.post("/new_user", response_model=User)
async def create_user(user: User):
    # Generate a new ID for the new user
    new_user_id = max(user.id for user in user_list) + 1 if user_list else 1
    user.id = new_user_id
    
    # Add the new user to user_list
    user_list.append(user)
    
    return user