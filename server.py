# from flask import Flask

# app = Flask(__name__)


# @app.route("/calculator/greeting", methods=['GET'])
# def greeting():
#     return ''

# @app.route("/calculator/add", methods=['POST'])
# def add():
#     return ''

# @app.route("/calculator/subtract", methods=['POST'])
# def subtract():
#     return ''

# if __name__ == '__main__':
#     app.run(port=8080,host='0.0.0.0')


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
