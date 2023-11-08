from fastapi import FastAPI
import random

# uvicorn main:app --reload 
# http://127.0.0.1:8000/docs

app = FastAPI()

@app.get('/')
async def root():
    return {'example': 'This is an example', 'data': 999}

@app.get('/random')
async def get_random():
    return {'number': random.randint(0, 100), 'limit': 100}

@app.get('/random/{limit}')
async def get_random(limit: int):
    return {'number': random.randint(0, 100), 'limit': limit}