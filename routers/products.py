from fastapi import APIRouter
from typing import List

product_list: List = ["Product 1","Product 2"]

router = APIRouter(prefix="/products",tags=["Products"])

# Get Product List
@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id: int):
    return product_list[id]
