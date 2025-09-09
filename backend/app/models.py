# backend/app/models.py
from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from .db import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)
