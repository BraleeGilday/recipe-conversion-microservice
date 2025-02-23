# Defines request/response schemas

from pydantic import BaseModel
from typing import List, Optional


# Define the Ingredient model
class Ingredient(BaseModel):
    name: str
    quantity: float
    unit: str


# Define the request model
class ConversionRequest(BaseModel):
    ingredients: List[Ingredient]
    serving_size: Optional[float] = None
    conversion_system: Optional[str] = None
