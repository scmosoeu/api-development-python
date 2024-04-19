from pydantic import BaseModel, validator
from typing import List

from .transactions import TotalKgSold, TotalQuantitySold, TotalValueSold

class CommoditySales(BaseModel):
    commodity: str
    total_value_sold: TotalValueSold
    total_quantity_sold: TotalQuantitySold
    total_kg_sold: TotalKgSold
    quantity_available: int


class DailyCommoditySales(BaseModel):
    information_date: str
    daily_prices: CommoditySales