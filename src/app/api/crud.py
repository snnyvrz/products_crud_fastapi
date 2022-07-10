from app.api.models import ProductSchema
from app.db import products, database


async def post(payload: ProductSchema):
    query = products.insert().values(
        title=payload.title,
        description=payload.description,
        category=payload.category,
        image=payload.image,
        price=payload.price,
    )
    return await database.execute(query=query)


async def get(id: int):
    query = products.select().where(id == products.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = products.select()
    return await database.fetch_all(query=query)
