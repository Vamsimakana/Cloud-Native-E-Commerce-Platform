# backend/app/schemas.py
from pydantic import BaseModel

class ProductOut(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    in_stock: bool
    class Config:
        orm_mode = True
