from typing import List

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


@router.get("/{id}/", response_model=ProductDB)
async def read_product(id: int):
    product = await crud.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/", response_model=List[ProductDB])
async def read_all_procuts():
    return await crud.get_all()


@router.put("/{id}/", response_model=ProductDB)
async def update_product(id: int, payload: ProductSchema):
    product = await crud.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_id = await crud.put(id, payload)

    response_object = {
        "id": product_id,
        "title": payload.title,
        "description": payload.description,
        "image": payload.image,
        "category": payload.category,
        "price": payload.price,
    }
    return response_object


@router.delete("/{id}/", response_model=ProductDB)
async def delete_product(id: int):
    product = await crud.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await crud.delete(id)

    return product
