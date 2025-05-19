from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str
    email: EmailStr
    name: str

class Student(BaseModel):
    id: str
    name: str