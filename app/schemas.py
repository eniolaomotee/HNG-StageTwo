from datetime import datetime
from typing import List
from pydantic import BaseModel


class PersonBaseSchema(BaseModel):
    name: str


    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


