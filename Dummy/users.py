from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from typing import List

router = APIRouter(prefix="/users",tags=["Users"])

class User(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    email: str

user_list: List[User] = [
            User(id=1, name="Alice", age=30, email="alice@example.com"),
            User(id=2, name="Bob", age=24, email="bob@example.com"),
            User(id=3, name="Charlie", age=29, email="charlie@example.com"),
            User(id=4, name="Diana", age=35, email="diana@example.com"),
            User(id=5, name="Eve", age=28, email="eve@example.com"),
            User(id=6, name="Frank", age=33, email="frank@example.com"),
            User(id=7, name="Grace", age=27, email="grace@example.com"),
            User(id=8,name="Tester", age=34, email="test@example.com")
                        ]

#--------------------- METHODS ---------------------#

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

#--------------------- FUNCTIONS ---------------------#
def user_filter(filter_type: str, user_ids: List[int] = None, start_id: int = None, end_id: int = None):
    
    if filter_type == "list" and user_ids is not None:
        filtered_users = [user for user in user_list if user.id in user_ids]
        error_message = "No users found with the provided IDs"

    elif filter_type == "range" and start_id is not None and end_id is not None:
        filtered_users = [user for user in user_list if start_id <= user.id <= end_id]
        error_message = "No users found within the provided range"
        
    else:
        raise HTTPException(status_code=400, detail="Invalid filter type or missing parameters")
    
    if not filtered_users:
            raise HTTPException(status_code=404, detail=error_message)
    return filtered_users