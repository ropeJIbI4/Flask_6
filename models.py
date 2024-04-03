from datetime import datetime
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(max_length=60)
    surname: str = Field(max_length=60)
    email: str = Field(max_length=128)
    password: str = Field(min_length=5)


class ProductCreate(BaseModel):
    title: str = Field(max_length=60)
    description: str = Field(max_length=60)
    price: int = Field(default=0)


class OrderCreate(BaseModel):
    user_id: int
    prod_id: int
    date: datetime = Field(default=datetime.now())
    status: str = Field(default="создан")


class UserRead(UserCreate):
    id: int

class OrderRead(OrderCreate):
    id: int

class ProductRead(ProductCreate):
    id: int
