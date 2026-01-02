from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Dict, Any
from datetime import datetime


class DeliveryAddressSchema(BaseModel):
    street_address: str
    ward: Optional[str] = None
    province_city: str
    recipient_name: str
    recipient_phone: str


class OrderItemSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    order_id: int
    product_id: int
    product_name: str
    size: Optional[int] = None
    color: Optional[str] = None
    quantity: int
    price_at_purchase: float


class CreateOrderItemSchema(BaseModel):
    product_id: int
    product_name: str
    size: Optional[int] = None
    color: Optional[str] = None
    quantity: int
    price_at_purchase: float


class OrderSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    user_id: int
    delivery_address: Dict[str, Any]  # JSON field
    order_date: datetime
    total_amount: float
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    items: Optional[List[OrderItemSchema]] = None


class CreateOrderSchema(BaseModel):
    delivery_address: DeliveryAddressSchema
    items: List[CreateOrderItemSchema]


class UpdateOrderSchema(BaseModel):
    delivery_address: Optional[DeliveryAddressSchema] = None
    status: Optional[str] = None
    total_amount: Optional[float] = None

