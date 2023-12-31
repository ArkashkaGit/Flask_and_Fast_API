import uvicorn
from db.db import database
from fastapi import FastAPI

from entity import users
from entity import products
from entity import orders
from entity import home

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router, tags=["users"])
app.include_router(products.router, tags=["products"])
app.include_router(orders.router, tags=["orders"])
app.include_router(home.router, tags=["home"])

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)