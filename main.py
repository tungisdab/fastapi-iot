from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, auth
import uvicorn
import pyrebase
from models.model import SignUpSchema, SignInSchema
from models.user_model import ParkingEntry
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from firebase_admin import initialize_app, db
from datetime import datetime

app = FastAPI(
    description="IOT Parking API",
    title="IOT Parking Database",
    docs_url="/",
)


if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://iot-fastapi-default-rtdb.asia-southeast1.firebasedatabase.app/"})


firebaseConfig = {
  "apiKey": "AIzaSyAoDLudOKMMhHwkqFzwvvvFtw0-RJO1ghE",
  "authDomain": "iot-fastapi.firebaseapp.com",
  "projectId": "iot-fastapi",
  "storageBucket": "iot-fastapi.appspot.com",
  "messagingSenderId": "923373532569",
  "appId": "1:923373532569:web:9e6381b5f5b95fec530f08",
  "measurementId": "G-3XFKEW63HW",
  "databaseURL": "https://iot-fastapi-default-rtdb.asia-southeast1.firebasedatabase.app/"
};

firebase = pyrebase.initialize_app(firebaseConfig)


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# @app.get('/')
# async def root():
#     return {'example': 'This is an example', 'data': 999}



@app.post("/update_parking_space")
async def update_parking_space(space_id: str, is_occupied: bool):
    try:
        # Cập nhật trạng thái vị trí đỗ xe lên Firebase
        ref = db.reference('/parking_spaces')
        ref.child(space_id).set(is_occupied)

        return {"message": f"Đã cập nhật trạng thái của vị trí {space_id} thành {is_occupied}."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi cập nhật vị trí: {str(e)}")
    
def get_parking_space_status(space_id: str):
    try:
        # Truy vấn trạng thái vị trí đỗ xe từ Realtime Database
        ref = db.reference(f'/parking_spaces/{space_id}')
        space_status = ref.get()
        return space_status
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting parking space status: {str(e)}")

@app.get("/get_parking_space_status/{space_id}")
async def get_parking_space(space_id: str):
    try:
        # Gọi hàm để lấy trạng thái vị trí đỗ xe
        space_status = get_parking_space_status(space_id)
        return space_status
    except HTTPException as e:
        return e
    

@app.post("/add_user")
async def add_user(user_id: str, user_name: str, email: str, phone_number: str):
    try:
        # Thêm thông tin người dùng vào Firebase
        ref = db.reference('/users')
        ref.child(user_id).set({
            "user_name": user_name,
            "email": email,
            "phone_number": phone_number,
        })

        return {"message": "User added successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding user: {str(e)}")
    
@app.get("/get_user/{user_id}")
async def get_user(user_id: str):
    try:
        # Truy vấn thông tin người dùng từ Firebase
        ref = db.reference(f'/users/{user_id}')
        user = ref.get()
        if user:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting user: {str(e)}")

@app.post("/add_parking_entry/{user_id}/{vehicle_id}")
async def add_parking_entry(
    user_id: str,
    vehicle_id: str,
    parking_entry: ParkingEntry,
    is_parked: bool 
):

    try:
        # Thêm thời gian ra vào vào Firebase
        ref = db.reference(f'/users/{user_id}/vehicles/{vehicle_id}/parking_entries')
        new_entry_ref = ref.push()
        new_entry_ref.set({
            "entry_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "is_parked": ParkingEntry.is_parked
        })

        return {"message": "Parking entry added successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding parking entry: {str(e)}")


@app.post('/signup')
async def signup(user_data:SignUpSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.create_user(
            email= email,
            password= password
        )

        return JSONResponse(content={"message": f"User created successfully. {user.uid}"}, status_code=201)
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail= f"Email already exists. {email}"
        )

@app.post('/signin')
async def signin(user_data:SignInSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = firebase.auth().sign_in_with_email_and_password(
            email = email,
            password = password
        )
        
        token = user['idToken']
        return JSONResponse(
            content={
                "token": token 
            },
            status_code=200
        )
    
    except:
        raise HTTPException(
            status_code=400,
            detail= "Email or password is incorrect."
        )

@app.post('/ping')
async def validate_token(request: Request):
    headers = request.headers
    jwt = headers.get('authorization')

    user = auth.verify_id_token(jwt)

    return user["user_id"]
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)