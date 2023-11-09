from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import random

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get('/')
async def root():
    return {'example': 'This is an example', 'data': 999}

@app.get('/random')
async def get_random():
    return {'number': random.randint(0, 100), 'limit': 100}

@app.get('/random/{limit}')
async def get_random(limit: int):
    return {'number': random.randint(0, 100), 'limit': limit}

# http://127.0.0.1:8000/items/53?q=khanh
@app.get('/items/{item_id}')
def get_items(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}

# http://127.0.0.1:8000/items/55?name=khanh&price=33
@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    return {'item_name': item.pr, "item_id": item_id}