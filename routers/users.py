from fastapi import APIRouter, HTTPException, status, Query
from typing import List
from database.models.user import User
from database.schemas.user import user_schema, users_schema
from database.atlas_server import dbclient
from bson import ObjectId

router = APIRouter(prefix="/users",tags=["Users"])

#-------------------------- METHODS --------------------------#

@router.get("/", response_model=List[User])
async def users():
    return users_schema(dbclient.users.find())

@router.get("/{id}")  # Path
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Method to add new users to the data_base file
@router.post("/", response_model=User,status_code=201)
async def create_user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail= "The user is already registered")

    user_dict = dict(user)
    del user_dict["id"]

    # Add the new user to user_list
    id = dbclient.users.insert_one(user_dict).inserted_id
    new_user = user_schema(dbclient.users.find_one({"_id": id}))
    
    return new_user

# PUT method to update user details
@router.put("/", response_model=User)
async def update_user(user: User):
    try:
        user_dict = dict(user)
        del user_dict["id"]
        dbclient.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        # If user_id not found, raise HTTPException with 404 Not Found
        raise HTTPException(status_code=404, detail="User not found. No Update made")
    return search_user("_id", ObjectId(user.id))

# DELETE method to erase users from MongoDB
@router.delete("/")
async def delete_users(user_ids: List[str] = Query(...)):
    deleted_users = []
    for user_id in user_ids:
        try:
            object_id = ObjectId(user_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid ObjectId: {user_id}")

        result = dbclient.users.find_one_and_delete({"_id": object_id})
        if result:
            deleted_users.append(user_schema(result))

    if not deleted_users:
        raise HTTPException(status_code=404, detail="No users found with the provided IDs")
    
    return {"message": "Users deleted successfully", "deleted_users": deleted_users}

#-------------------------- FUNCTIONS --------------------------#

def search_user(field: str, key):
    try:
        user = dbclient.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}