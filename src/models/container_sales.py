from pydantic import BaseModel, validator
from typing import List

from .transactions import TotalKgSold, TotalQuantitySold, TotalValueSold

class ContainerSales(BaseModel):
    container: str
    quantity_available: int
    value_sold: TotalValueSold
    quantity_sold: TotalQuantitySold
    kg_sold: TotalKgSold
    


class DailyContainerSales(BaseModel):
    information_date: str
    commodity: str
    daily_prices: List[ContainerSales]