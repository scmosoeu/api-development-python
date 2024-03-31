from bs4 import BeautifulSoup
from typing import Union

from common.clean_string_helper import remove_character, strip_whitespaces
from common.extract_values_helper import get_current_value
from common.numeric_conversion_helper import convert_to_numeric

from models.container_sales import ContainerSales, DailyContainerSales
from .get_transactions import get_commodity_information, get_value_sold, get_quantity_sold, get_kg_sold


def get_container_sales(commodity: str, soup: BeautifulSoup) -> ContainerSales:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    results = get_commodity_information(commodity, soup)
    container = results[0].text
    quantity_available = remove_character(results[1].text, ',')
    average_price_per_kg = remove_character(results[1].text, 'R')

    return ContainerSales(
        container=container,
        quantity_available=quantity_available,
        value_sold=get_value_sold(commodity.lower(), 2, soup),
        quantity_sold=get_quantity_sold(commodity.lower(), 3, soup),
        quantity_sold=get_kg_sold(commodity.lower(), 4, soup),
        kg_sold=convert_to_numeric(quantity_available, 'int'),
        average_price_per_kg=average_price_per_kg
    )


def get_daily_container_sales(commodity: str, soup: BeautifulSoup) -> DailyContainerSales:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    information_date = soup.select_one('#right2 p b').text

    return DailyContainerSales(
        information_date=information_date,
        daily_prices=get_commodity_sales(commodity, soup)
    )
    