from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials
import random
import uvicorn
import pyrebase

app = FastAPI(
    description="IOT Parking API",
    title="IOT Parking Database",
    docs_url="/",
)


if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

firebaseConfig = {
  "apiKey": "AIzaSyAoDLudOKMMhHwkqFzwvvvFtw0-RJO1ghE",
  "authDomain": "iot-fastapi.firebaseapp.com",
  "projectId": "iot-fastapi",
  "storageBucket": "iot-fastapi.appspot.com",
  "messagingSenderId": "923373532569",
  "appId": "1:923373532569:web:9e6381b5f5b95fec530f08",
  "measurementId": "G-3XFKEW63HW",
  "databaseURL": ""
};

firebase = pyrebase.initialize_app(firebaseConfig)



class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# @app.get('/')
# async def root():
#     return {'example': 'This is an example', 'data': 999}

@app.get('/random')
async def get_random():
    return {'number': random.randint(0, 100), 'limit': 100}

@app.get('/random/{limit}')
async def get_random(limit: int):
    return {'number': random.randint(0, limit), 'limit': limit}

# http://127.0.0.1:8000/items/53?q=khanh
@app.get('/items/{item_id}')
def get_items(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}

# http://127.0.0.1:8000/items/55?name=khanh&price=33
@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    return {'item_name': item.pr, "item_id": item_id}


    
@app.post('/signup')
async def signup():
    pass

@app.post('/signin')
async def signin():
    pass

@app.post('/ping')
async def ping():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)