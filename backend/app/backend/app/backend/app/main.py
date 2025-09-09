# backend/app/main.py
from fastapi import FastAPI, Depends
from .db import SessionLocal, engine, Base
from .models import Product
from .schemas import ProductOut

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ecom API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def seed():
    db = SessionLocal()
    if db.query(Product).count() == 0:
        db.add_all([
            Product(name="T-shirt", description="Comfortable cotton tee", price=19.99),
            Product(name="Sneakers", description="Running shoes", price=79.99),
            Product(name="Backpack", description="Laptop backpack", price=49.99),
        ])
        db.commit()
    db.close()

@app.get("/products", response_model=list[ProductOut])
def products(db=Depends(get_db)):
    return db.query(Product).all()

@app.get("/health")
def health():
    return {"status":"ok"}
