from typing import Optional
from pydantic import BaseModel,Field
import re

class Employee(BaseModel):
    id:int
    name:str=Field(
        ...,
        min_length=3,
        max_length=50,
        description='Employee Name',
        examples='Hitesh Choudhary'
    )
    department:Optional[str]='General'
    salary:float=Field(
        ...,
        ge=10000,
        le=1000000,
        description='Annual salary in usd'
    )
    
class User(BaseModel):
    email: str = Field(..., regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    phone: str = Field(..., regex=r'^\+?[1-9]\d{1,14}$')
    age: int = Field(..., gt=0,lt=150,description='Age in year')
    discount: float = Field(default=0.0, ge=0.0, le=1.0)
    
    