from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

user_list = [User(id=1, name="Alice", age=30, email="alice@example.com"),
             User(id=2, name="Bob", age=24, email="bob@example.com"),
             User(id=3, name="Charlie", age=29, email="charlie@example.com"),
             User(id=4, name="Diana", age=35, email="diana@example.com"),
             User(id=5, name="Eve", age=28, email="eve@example.com"),
             User(id=6, name="Frank", age=33, email="frank@example.com"),
             User(id=7, name="Grace", age=27, email="grace@example.com"),
             User(id=200,name="Chavito", age=34, email="elchavito@example.com")]