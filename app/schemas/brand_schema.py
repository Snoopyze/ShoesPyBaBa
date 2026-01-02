from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class BrandSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    brand_name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CreateBrandSchema(BaseModel):
    brand_name: str
    description: Optional[str] = None


class UpdateBrandSchema(BaseModel):
    brand_name: Optional[str] = None
    description: Optional[str] = None

