from app.models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm import Session

class Role(BaseModel):
    __tablename__ = "role"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, index=True, default=func.now())
    updated_at = Column(DateTime, index=True, default=func.now(), onupdate=func.now())


def seed_roles(db: Session):
    # Check if roles already exist
    existing_roles = db.query(Role).count()
    
    if existing_roles == 0:
        roles = [
            Role(name="admin", description="Administrator with full access"),
            Role(name="user", description="Regular user with limited access")
        ]
        
        db.add_all(roles)
        db.commit()
        print("✓ Roles seeded successfully!")
    else:
        print("✓ Roles already exist, skipping seed.")