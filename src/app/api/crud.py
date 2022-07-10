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
