from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    first: int
    second: int


@app.get("/calculator/greeting")
def greeting():
    return {"result": "Hello world!"}


@app.post("/calculator/add")
def add(item: Item):
    result = item.first + item.second
    return {"result": result}


@app.post("/calculator/subtract")
def subtract(item: Item):
    result = item.first - item.second
    return {"result": result}
