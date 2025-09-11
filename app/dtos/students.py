from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class CreateStudentDto(BaseModel):
    name: str = Field(max_length=254)
    email: EmailStr


class UpdateStudentDto(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
