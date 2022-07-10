from pydantic import BaseModel


class ProductSchema(BaseModel):
    title: str
    description: str
    image: str
    category: str
    price: float


class ProductDB(ProductSchema):
    id: int
