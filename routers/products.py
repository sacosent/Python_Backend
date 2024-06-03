from fastapi import APIRouter
from data_base import product_list

router = APIRouter()

# Get Product List
@router.get("/products")
async def products():
    return product_list

@router.get("/products/{id}")
async def products(id: int):
    return product_list[id]