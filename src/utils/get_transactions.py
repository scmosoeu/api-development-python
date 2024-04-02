from bs4 import BeautifulSoup
from fastapi import HTTPException, status

from common.clean_string_helper import remove_character, strip_whitespaces
from common.extract_values_helper import get_current_value
from common.numeric_conversion_helper import convert_to_numeric
from models.transactions import TotalKgSold, TotalQuantitySold, TotalValueSold

def get_commodity_information(commodity: str, soup: BeautifulSoup) -> list:
    """
    Extract information for the selected commodity

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """

    results = soup.find_all(
        class_='tleft2',
        string=lambda text: commodity == text.lower()
    )

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{commodity} does not exist.'
        )

    return results[0].parent.find_all('td')


def get_commodity_containers_information(soup: BeautifulSoup) -> list:
    """
    Extract information for the selected commodity

    Args
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """
    
    results = soup.find_all('tr')

    return results


def get_commodity_value(commodity: str, soup: BeautifulSoup) -> list:
    """
    Extract the value parameter of the selected commodity from the
    drop down

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when 
    extracting data
    """
    
    results = soup.find('select')
    commodity_element = results.find_all(
        'option', string=lambda text: commodity == text.lower()
    )

    if not commodity_element:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{commodity} does not exist.'
        )

    commodity_value = commodity_element[0].get('value')

    return commodity_value


def process_values_with_mtd(input_string: str, index_loc: int) -> str:
    
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


def get_value_sold_commodity(element_tags: list, index_loc: int) -> TotalValueSold:
    """
    Extract the parameters for total value sold

    Args
    element_tags - A list of element tags to extract information from
    index_loc - Index location of the extracted value
    """

    value_sold_params = element_tags[index_loc].text
    value_sold = process_values_with_mtd(value_sold_params, 0)
    month_to_date = process_values_with_mtd(value_sold_params, 1)

    return TotalValueSold(
        value_sold=convert_to_numeric(value_sold, 'float'),
        month_to_date=convert_to_numeric(month_to_date, 'float')
    )


def get_value_sold_container(element_tags: list, index_loc: int) -> TotalValueSold:
    """
    Extract the parameters for value sold

    Args
    element_tags - A list of element tags to extract information from
    index_loc - Index location of the extracted value
    """

    value_sold_params = element_tags[index_loc].text
    value_sold = process_values_with_mtd(value_sold_params, 0)
    month_to_date = process_values_with_mtd(value_sold_params, 1)

    return TotalValueSold(
        value_sold=convert_to_numeric(value_sold, 'float'),
        month_to_date=convert_to_numeric(month_to_date, 'float')
    )


def get_quantity_sold_commodity(element_tags: list, index_loc: int) -> TotalQuantitySold:
    """
    Extract the parameters for total quantity sold

    Args
    element_tags - A list of element tags to extract information from
    index_loc - Index location of the extracted value
    """

    qty_params = element_tags[index_loc].text
    
    qty_sold = process_values_with_mtd(qty_params, 0)
    month_to_date = process_values_with_mtd(qty_params, 1)

    return TotalQuantitySold(
        quantity_sold=convert_to_numeric(qty_sold, 'int'),
        month_to_date=convert_to_numeric(month_to_date, 'int')
    )


def get_quantity_sold_container(element_tags: list, index_loc: int) -> TotalQuantitySold:
    """
    Extract the parameters for total quantity sold

    Args
    element_tags - A list of element tags to extract information from
    index_loc - Index location of the extracted value
    """

    qty_params = element_tags[index_loc].text
    
    qty_sold = process_values_with_mtd(qty_params, 0)
    month_to_date = process_values_with_mtd(qty_params, 1)

    return TotalQuantitySold(
        quantity_sold=convert_to_numeric(qty_sold, 'int'),
        month_to_date=convert_to_numeric(month_to_date, 'int')
    )


def get_kg_sold_commodity(element_tags: list, index_loc: int) -> TotalKgSold:
    """
    Extract the parameters for total kg sold

    Args
    element_tags - A list of element tags to extract information from
    index_loc - Index location of the extracted value
    """

    kg_params = element_tags[index_loc].text

    kg_sold = process_values_with_mtd(kg_params, 0)
    month_to_date = process_values_with_mtd(kg_params, 1)

    return TotalKgSold(
        kg_sold=convert_to_numeric(kg_sold, 'float'),
        month_to_date=convert_to_numeric(month_to_date, 'float')
    )


def get_kg_sold_container(element_tags: list, index_loc: int) -> TotalKgSold:
    """
    Extract the parameters for total kg sold

    Args
    element_tags - A list of element tags to extract information from
    index_loc - Index location of the extracted value
    """

    kg_params = element_tags[index_loc].text

    kg_sold = process_values_with_mtd(kg_params, 0)
    month_to_date = process_values_with_mtd(kg_params, 1)

    return TotalKgSold(
        kg_sold=convert_to_numeric(kg_sold, 'float'),
        month_to_date=convert_to_numeric(month_to_date, 'float')
    )