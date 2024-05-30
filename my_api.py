from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from user_db import User, user_list

app = FastAPI()

#--------------------- USER LOGIN ---------------------#

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/users", response_model=List[User])
async def users():
    return user_list

@app.get("/users/listfilter", response_model=List[User])
def get_users_by_ids(user_ids: Optional[List[int]] = Query(None)):
    if not user_ids:
        return user_list
    
    filtered_users = [user for user in user_list if user.id in user_ids]
    
    if not filtered_users:
        raise HTTPException(status_code=404, detail="No users found with the provided IDs")
    
    return filtered_users

@app.get("/users/rangefilter", response_model=List[User])
def get_users_by_range(start_id: int, end_id: int):
    filtered_users = [user for user in user_list if start_id <= user.id <= end_id]
    
    if not filtered_users:
        raise HTTPException(status_code=404, detail="No users found within the provided range")
    
    return filtered_users