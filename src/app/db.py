import os

from sqlalchemy import (
    Column,
    Float,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(128)),
    Column("description", String(1024)),
    Column("price", Float),
    Column("image", String(128)),
    Column("category", String(128)),
)

# databases query builder
database = Database(DATABASE_URL)
