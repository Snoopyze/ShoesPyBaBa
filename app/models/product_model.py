from app.models.base_model import BaseModel
from sqlalchemy import Column, String, Float, DateTime, Integer
import datetime

class Product(BaseModel):
    __tablename__ = "products"
    
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), index=True)
    description: str = Column(String(1000), index=True)
    price: float = Column(Float, index=True)
    deleted_at: datetime.datetime = Column(DateTime, index=True, nullable=True)