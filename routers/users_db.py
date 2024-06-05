from fastapi import APIRouter, HTTPException, Query
from typing import List
from data_base import User, user_list, user_filter

router = APIRouter(prefix="/users",tags=["Users"])

#--------------------- USER LOGIN ---------------------#

@router.get("/", response_model=List[User])
async def users():
    return user_list

@router.get("/listfilter", response_model=List[User])
async def get_users_by_ids(user_ids: List[int] = Query(...)):
    
    filtered_users = user_filter(filter_type="list", user_ids=user_ids)
    return filtered_users

@router.get("/rangefilter", response_model=List[User])
async def get_users_by_range(start_id: int, end_id: int):
    
    filtered_users = user_filter(filter_type="range", start_id=start_id, end_id=end_id)
    return filtered_users

# Method to add new users to the data_base file
@router.post("/", response_model=User,status_code=201)
async def create_user(user: User):
    # Generate a new ID for the new user
    new_user_id = max(user.id for user in user_list) + 1 if user_list else 1
    user.id = new_user_id
    
    # Add the new user to user_list
    user_list.append(user)
    
    return user

# PUT method to update user details
@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_data: dict):
    for user in user_list:
        if user.id == user_id:
            for key, value in user_data.items():
                setattr(user, key, value)
            return user
    
    # If user_id not found, raise HTTPException with 404 Not Found
    raise HTTPException(status_code=404, detail="User not found. No Update made")

# DELETE method to erase users from user_db
@router.delete("/")
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