from pydantic import BaseModel, validator

class TotalValueSold(BaseModel):
    value_sold: float
    month_to_date: float 


class TotalQuantitySold(BaseModel):
    quantity_sold: int
    month_to_date: int


class TotalKgSold(BaseModel):
    kg_sold: float
    month_to_date: float 