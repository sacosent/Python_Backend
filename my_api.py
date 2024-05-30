from fastapi import FastAPI, HTTPException, Query
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
async def get_users_by_ids(user_ids: List[int] = Query(...)):
    
    filtered_users = user_filter(filter_type="list", user_ids=user_ids)
    return filtered_users

@app.get("/users/rangefilter", response_model=List[User])
async def get_users_by_range(start_id: int, end_id: int):
    
    filtered_users = user_filter(filter_type="range", start_id=start_id, end_id=end_id)
    return filtered_users

# Method to add new users to the user_db file
@app.post("/new_user", response_model=User)
async def create_user(user: User):
    # Generate a new ID for the new user
    new_user_id = max(user.id for user in user_list) + 1 if user_list else 1
    user.id = new_user_id
    
    # Add the new user to user_list
    user_list.append(user)
    
    return user

# PUT method to update user details
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_data: dict):
    for user in user_list:
        if user.id == user_id:
            for key, value in user_data.items():
                setattr(user, key, value)
            return user
    
    # If user_id not found, raise HTTPException with 404 Not Found
    raise HTTPException(status_code=404, detail="User not found. No Update made")

# DELETE method to erase users from user_db
@app.delete("/users")
async def delete_users(user_ids: List[int] = Query(...)):
    deleted_users = []
    for user_id in user_ids:
        for user in user_list:
            if user.id == user_id:
                user_list.remove(user)
                deleted_users.append(user)
                break
    
    if not deleted_users:
        raise HTTPException(status_code=404, detail="No users found with the provided IDs")
    
    return {"message": "Users deleted successfully", "deleted_users": deleted_users}