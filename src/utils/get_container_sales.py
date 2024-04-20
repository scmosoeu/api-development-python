from bs4 import BeautifulSoup
from typing import List

from common.clean_string_helper import remove_character
from common.numeric_conversion_helper import convert_to_numeric

from models.container_sales import ContainerSales, DailyContainerSales
from get_transactions import get_commodity_containers_information, get_value_sold_container, get_quantity_sold_container, get_kg_sold_container


def get_container_sales(soup: BeautifulSoup) -> List[ContainerSales]:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when
    extracting data
    """

    results = get_commodity_containers_information(soup)

    container_sales = []

    for i in range(1, len(results)):

        row = results[i].find_all('td')

        container = row[0].text
        quantity_available = remove_character(row[1].text, ',')
        average_price_per_kg = remove_character(row[-1].text, 'R')

        container_sale = ContainerSales(
            container=container,
            quantity_available=convert_to_numeric(quantity_available, 'int'),
            total_value_sold=get_value_sold_container(row, 2),
            total_quantity_sold=get_quantity_sold_container(row, 3),
            total_kg_sold=get_kg_sold_container(row, 4),
            average_price_per_kg=convert_to_numeric(average_price_per_kg, 'float')
        )

        container_sales.append(container_sale.model_dump())

    return container_sales


def get_daily_container_sales(commodity: str, soup: BeautifulSoup) -> DailyContainerSales:
    """
    Extract the parameters for each commodity sales

    Args
    commodity - The commodity information that is being extracted
    soup - A BeautifulSoup object to be queried when
    extracting data
    """

    information_date = soup.select_one('#right2 p b').text

    container_sales = get_container_sales(soup)

    return DailyContainerSales(
        information_date=information_date,
        commodity=commodity,
        daily_prices=container_sales
    )
