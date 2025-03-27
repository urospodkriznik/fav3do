from fastapi import FastAPI
from app.db import database
from app.models import items, metadata
import sqlalchemy
import os

app = FastAPI()

engine = sqlalchemy.create_engine(os.getenv("DB_URL"))
metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()
    query = items.select()
    existing = await database.fetch_all(query)
    if not existing:
        await database.execute_many(query=items.insert(), values=[
            {"name": "Item A"},
            {"name": "Item B"},
            {"name": "Item C"},
            {"name": "Item D"}
        ])

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/api/items")
async def get_items():
    query = items.select()
    return await database.fetch_all(query)