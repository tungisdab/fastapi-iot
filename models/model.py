from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "example@2example.com",
                "password": "example1222222"
            }
        }

class SignInSchema(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "example@2example.com",
                "password": "example1222222"
            }
        }