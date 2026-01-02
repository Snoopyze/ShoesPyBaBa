from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from app.models.base_model import BaseModel


class Brand(BaseModel):
    __tablename__ = "brands"
    
    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, index=True, default=datetime.now)
    updated_at = Column(DateTime, index=True, default=datetime.now, onupdate=datetime.now)

