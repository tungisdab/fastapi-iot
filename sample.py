import requests

requests = requests.get('http://127.0.0.1:8000/items/53')
print(requests.json())