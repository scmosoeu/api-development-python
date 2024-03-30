from bs4 import BeautifulSoup

from common.get_values import convert_to_numeric, get_current_value, get_mtd_value
from models.commodity_sales import (
    TotalKgSold, TotalValueSold, TotalQuantitySold, CommoditySales, DailySales
)

def get_commodity(commodity: str, soup: BeautifulSoup) -> list:
    """
    Extract information for the selected commodity

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """
    
    results = soup.find_all(
        class_='tleft2',
        string=lambda text: commodity in text.lower()
    )[0]

    return results.parent.find_all('td')

def get_value_sold(commodity: str, soup: BeautifulSoup) -> TotalValueSold:
    """
    Extract the parameters for total value sold

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    results = get_commodity(commodity, soup)

    value_sold_params = results[1].text
    value_sold = get_current_value(value_sold_params, 'MTD:', 'R')
    month_to_date = get_mtd_value(value_sold_params, 'MTD:', 'R')

    return TotalValueSold(
        value_sold=value_sold,
        month_to_date=month_to_date
    )


def get_quantity_sold(commodity: str, soup: BeautifulSoup) -> TotalQuantitySold:
    """
    Extract the parameters for total quantity sold

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """


    results = get_commodity(commodity, soup)

    qty_params = results[2].text

    qty_sold = get_current_value(qty_params, 'MTD:')
    month_to_date = get_mtd_value(qty_params, 'MTD:')

    return TotalQuantitySold(
        quantity_sold=convert_to_numeric(qty_sold, 'int'),
        month_to_date=convert_to_numeric(month_to_date, 'int')
    )


def get_kg_sold(commodity: str, soup: BeautifulSoup) -> TotalKgSold:
    """
    Extract the parameters for total kg sold

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    results = get_commodity(commodity, soup)

    kg_params = results[3].text

    kg_sold = get_current_value(kg_params, 'MTD:')
    month_to_date = get_mtd_value(kg_params, 'MTD:')

    return TotalKgSold(
        kg_sold=convert_to_numeric(kg_sold, 'float'),
        month_to_date=convert_to_numeric(month_to_date, 'float')
    )


def get_commodity_sales(commodity: str, soup: BeautifulSoup) -> CommoditySales:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    results = get_commodity(commodity, soup)
    quantity_available = results[-1].text.replace(',', '')

    return CommoditySales(
        commodity=commodity.lower(),
        total_value_sold=get_value_sold(commodity.lower(), soup),
        total_quantity_sold=get_quantity_sold(commodity.lower(), soup),
        total_kg_sold=get_kg_sold(commodity.lower(), soup),
        quantity_available=convert_to_numeric(quantity_available, 'int')
    )


def get_daily_sales(commodity: str, soup: BeautifulSoup) -> DailySales:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    information_date = soup.select_one('#right2 p b').text

    return DailySales(
        information_date=information_date,
        daily_prices=get_commodity_sales(commodity, soup)
    )
    