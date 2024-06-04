from fastapi import APIRouter
from data_base import product_list

router = APIRouter(prefix="/products",tags=["Products"])

# Get Product List
@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id: int):
    return product_list[id]
