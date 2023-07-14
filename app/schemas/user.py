from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class UserInDBBase(UserBase):
    id: int
    class Config:
        orm_mode = True