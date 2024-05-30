from http.client import HTTPException
from pydantic import BaseModel
from typing import List, Optional

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

