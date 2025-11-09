from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ContactMessage(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=2000)
    source: Optional[str] = Field(default="website", description="submission source")
