import requests


token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ0OWU0N2ZiZGQ0ZWUyNDE0Nzk2ZDhlMDhjZWY2YjU1ZDA3MDRlNGQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaW90LWZhc3RhcGkiLCJhdWQiOiJpb3QtZmFzdGFwaSIsImF1dGhfdGltZSI6MTY5OTYzNDA0OCwidXNlcl9pZCI6IjYzbEVFS0VBN2hhbW9IamhCUG1KTzVqazFYbzEiLCJzdWIiOiI2M2xFRUtFQTdoYW1vSGpoQlBtSk81amsxWG8xIiwiaWF0IjoxNjk5NjM0MDQ4LCJleHAiOjE2OTk2Mzc2NDgsImVtYWlsIjoiZXhhbXBsZUAyZXhhbXBsZS5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZXhhbXBsZUAyZXhhbXBsZS5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.HIe7Aqu413vgOVdb9gIC_bww6B6KyW5NOqq-3vtQAPeM4n7ZC3zghtt4f3Lj2jELAw6PYdghkER6VwdRruqNT8xIRq80ym_Hz4OMTDXBhnzTh3zEqUa2sZ7jTccFHO9Ud5UFQNQe4ukGiWo4GMP0SpPlvBvR1_CyBkl6fDV_AzwARGOYs5KIpK7iepryqRSBPf478WTUxHiBkVBWKEQauPSBacSNjP2zf8N6l5KVNDgVQ9Z6zKArzcMcZA0vNpaWNgXM6O-Szye1lsK7N2EpvzqyMncYF6xpNd1tMP-TYrkc_Y218bWjSDjf8kPlOwpjhtNXOlibxjKTGiYbvAfp3Q"

def test_validate_endpoint():
    headers = {
        'authorization': token
    }
    response = requests.post(
        "http://localhost:8000/ping",
        headers=headers
    )
    return response.text

print(test_validate_endpoint())

# {"iss":"https://securetoken.google.com/iot-fastapi",
#  "aud":"iot-fastapi",
#  "auth_time":1699634048,
#  "user_id":"63lEEKEA7hamoHjhBPmJO5jk1Xo1",
#  "sub":"63lEEKEA7hamoHjhBPmJO5jk1Xo1",
#  "iat":1699634048,
#  "exp":1699637648,
#  "email":"example@2example.com",
#  "email_verified":false,
#  "firebase":{"identities":{"email":["example@2example.com"]},"sign_in_provider":"password"},
#  "uid":"63lEEKEA7hamoHjhBPmJO5jk1Xo1"}

# @app.get('/random')
# async def get_random():
#     return {'number': random.randint(0, 100), 'limit': 100}

# @app.get('/random/{limit}')
# async def get_random(limit: int):
#     return {'number': random.randint(0, limit), 'limit': limit}

# # http://127.0.0.1:8000/items/53?q=khanh
# @app.get('/items/{item_id}')
# def get_items(item_id: int, q: Union[str, None] = None):
#     return {'item_id': item_id, 'q': q}

# # http://127.0.0.1:8000/items/55?name=khanh&price=33
# @app.put("/items/{item_id}")
# def save_item(item_id: int, item: Item):
#     return {'item_name': item.pr, "item_id": item_id}