from pydantic import BaseModel, ConfigDict
from typing import Optional


class AddressSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    user_id: Optional[int] = None
    street_address: str
    ward: Optional[str] = None
    province_city: str
    is_default: bool = False
    recipient_name: str
    recipient_phone: str


class CreateAddressSchema(BaseModel):
    street_address: str
    ward: Optional[str] = None
    province_city: str
    is_default: bool = False
    recipient_name: str
    recipient_phone: str


class UpdateAddressSchema(BaseModel):
    street_address: Optional[str] = None
    ward: Optional[str] = None
    province_city: Optional[str] = None
    is_default: Optional[bool] = None
    recipient_name: Optional[str] = None
    recipient_phone: Optional[str] = None

