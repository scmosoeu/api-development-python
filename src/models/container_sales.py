from pydantic import BaseModel, validator
from typing import List

from .transactions import TotalKgSold, TotalQuantitySold, TotalValueSold

class ContainerSales(BaseModel):
    commodity: str
    total_value_sold: TotalValueSold
    total_quantity_sold: TotalQuantitySold
    total_kg_sold: TotalKgSold
    quantity_available: int


class DailyContainerSales(BaseModel):
    information_date: str
    daily_prices: ContainerSales