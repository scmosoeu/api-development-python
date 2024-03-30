from bs4 import BeautifulSoup

from common.get_values import convert_to_numeric, get_current_value, get_mtd_value
from models.commodity_sales import (
    TotalKgSold, TotalValueSold, TotalQuantitySold, CommoditySales, DailySales
)

def get_value_sold(soup: BeautifulSoup) -> TotalValueSold:
    """
    Extract the parameters for total value sold

    Args
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    value_sold_params = soup.find(class_='tleft').text

    value_sold = get_current_value(value_sold_params, 'MTD:', 'R')
    month_to_date = get_mtd_value(value_sold_params, 'MTD:', 'R')

    return TotalValueSold(
        value_sold=value_sold,
        month_to_date=month_to_date
    )


def get_quantity_sold(soup: BeautifulSoup) -> TotalQuantitySold:
    """
    Extract the parameters for total quantity sold

    Args
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    qty_params = soup.find(class_='tleft').findNextSibling().text

    qty_sold = get_current_value(qty_params, 'MTD:')
    month_to_date = get_mtd_value(qty_params, 'MTD:')

    return TotalQuantitySold(
        kg_sold=convert_to_numeric(qty_sold, 'int'),
        month_to_date=convert_to_numeric(month_to_date, 'int')
    )


def get_kg_sold(soup: BeautifulSoup) -> TotalKgSold:
    """
    Extract the parameters for total kg sold

    Args
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    kg_params = soup.select_one('td:last-child').findPreviousSibling().text

    kg_sold = get_current_value(kg_params, 'MTD:')
    month_to_date = get_mtd_value(kg_params, 'MTD:')

    return TotalKgSold(
        kg_sold=convert_to_numeric(kg_sold, 'float'),
        month_to_date=convert_to_numeric(month_to_date, 'float')
    )


def get_commodity_sales(soup: BeautifulSoup) -> CommoditySales:
    """
    Extract the parameters each commodity sales

    Args
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    commodity = soup.find(class_='tleft2').text.lower()
    quantity_available = soup.select_one('td:last-child').get_text()

    return CommoditySales(
        commodity=commodity,
        total_value_sold=get_value_sold(soup),
        total_quantity_sold=get_quantity_sold(soup),
        total_kg_sold=get_kg_sold(soup),
        quantity_available=convert_to_numeric(quantity_available, 'int')
    )
    