from fastapi import APIRouter, HTTPException

from app.api import crud
from app.api.models import ProductDB, ProductSchema

router = APIRouter()


@router.post("/", response_model=ProductDB, status_code=201)
async def create_product(payload: ProductSchema):
    product_id = await crud.post(payload)

    response_object = {
        "id": product_id,
        "title": payload.title,
        "description": payload.description,
        "image": payload.image,
        "category": payload.category,
        "price": payload.price,
    }
    return response_object
