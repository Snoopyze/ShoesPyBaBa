from app.models.base_model import BaseModel
from sqlalchemy import Column, String, Float, DateTime, Integer
import datetime

class Product(BaseModel):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(500))  # Removed index to avoid key length limit
    price = Column(Float, index=True)
    deleted_at = Column(DateTime, index=True, nullable=True)