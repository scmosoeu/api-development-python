from pydantic import BaseModel, validator
from typing import List


class TotalValueSold(BaseModel):
    value_sold: float
    month_to_date: float 


class TotalQuantitySold(BaseModel):
    quantity_sold: int
    month_to_date: int


class TotalKgSold(BaseModel):
    kg_sold: float
    month_to_date: float 


class CommoditySales(BaseModel):
    commodity: str
    total_value_sold: TotalValueSold
    total_quantity_sold: TotalQuantitySold
    total_kg_sold: TotalKgSold
    quantity_available: int


class DailyCommoditySales(BaseModel):
    information_date: str
    daily_prices: CommoditySales