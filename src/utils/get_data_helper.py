from bs4 import BeautifulSoup
from typing import Union

from common.clean_string import remove_character, strip_whitespaces
from common.extract_values import get_current_value
from common.numeric_conversion import convert_to_numeric

from models.commodity_sales import (
    TotalKgSold, TotalValueSold, TotalQuantitySold, CommoditySales, DailyCommoditySales
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


def process_values_with_mtd(input_string: str, index_loc: int) -> Union[int, float]:
    
    """
    Get current numeric value from the input string

    Args:
    str_value - The string value upon which the current
        value is going to be extracted 
    index_loc - Location of the extracted value within an 
        iterable
    """

    output_string = get_current_value(input_string, 'MTD:', index_loc)
    output_string = remove_character(output_string, 'R', '')
    output_string = remove_character(output_string, ',', '')
    cleaned_string = strip_whitespaces(output_string)

    return cleaned_string



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
    value_sold = process_values_with_mtd(value_sold_params, 0)
    month_to_date = process_values_with_mtd(value_sold_params, 1)

    return TotalValueSold(
        value_sold=convert_to_numeric(value_sold, 'float'),
        month_to_date=convert_to_numeric(month_to_date, 'float')
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
    
    qty_sold = process_values_with_mtd(qty_params, 0)
    month_to_date = process_values_with_mtd(qty_params, 1)

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

    kg_sold = process_values_with_mtd(kg_params, 0)
    month_to_date = process_values_with_mtd(kg_params, 1)

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
    quantity_available = remove_character(results[-1].text, ',')

    return CommoditySales(
        commodity=commodity.lower(),
        total_value_sold=get_value_sold(commodity.lower(), soup),
        total_quantity_sold=get_quantity_sold(commodity.lower(), soup),
        total_kg_sold=get_kg_sold(commodity.lower(), soup),
        quantity_available=convert_to_numeric(quantity_available, 'int')
    )


def get_daily_sales(commodity: str, soup: BeautifulSoup) -> DailyCommoditySales:
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
    