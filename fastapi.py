from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

#--------------------- PRUEBA GENERAL
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id}

#--------------------- USER LOGIN

@app.get("/users")
async def users_json():
    return [{"name": "Santiago Cosentino",
             "age": 28,
             "email": "cosentinosantiago92@gmail.com",
             "username": "sacosent",
             "password": "queteimporta"}]