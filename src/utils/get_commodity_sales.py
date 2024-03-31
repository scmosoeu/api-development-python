from bs4 import BeautifulSoup
from typing import Union

from common.clean_string_helper import remove_character
from common.numeric_conversion_helper import convert_to_numeric

from models.commodity_sales import CommoditySales, DailyCommoditySales
from .get_transactions import get_commodity_information, get_value_sold, get_quantity_sold, get_kg_sold


def get_commodity_sales(commodity: str, soup: BeautifulSoup) -> CommoditySales:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    results = get_commodity_information(commodity, soup)
    quantity_available = remove_character(results[-1].text, ',')

    return CommoditySales(
        commodity=commodity.lower(),
        total_value_sold=get_value_sold(commodity.lower(), soup),
        total_quantity_sold=get_quantity_sold(commodity.lower(), soup),
        total_kg_sold=get_kg_sold(commodity.lower(), soup),
        quantity_available=convert_to_numeric(quantity_available, 'int')
    )


def get_daily_commodity_sales(commodity: str, soup: BeautifulSoup) -> DailyCommoditySales:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    information_date = soup.select_one('#right2 p b').text

    return DailyCommoditySales(
        information_date=information_date,
        daily_prices=get_commodity_sales(commodity, soup)
    )