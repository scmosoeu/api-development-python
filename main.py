import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI

from utils.get_commodity_sales import get_daily_commodity_sales
from utils.get_container_sales import get_daily_container_sales
from utils.get_transactions import get_commodity_value
from utils.page_connect_helper import load_page

app = FastAPI()

load_dotenv()
URL = os.getenv('BASE_URL')

@app.get('/{commodity}')
def get_commodity_sales(commodity: str) -> dict:
    """
    Get information of the specified commodity 
    for the day

    Args:
    commodity - The commodity name to display
        latest sales for
    """

    soup = load_page(URL)

    commodity_sales = get_daily_commodity_sales(commodity, soup)

    return commodity_sales.model_dump()


@app.get('/container/{commodity}')
def get_container_sales(commodity: str) -> dict:
    """
    Get information of the specified commodity 
    filtered by container type for the day

    Args:
    commodity - The commodity name to display
        latest sales for
    """

    base_soup = load_page(URL)

    # Extract the value parameter from the dropdown
    commodity_value = get_commodity_value(commodity, base_soup)

    # Follow up url link
    updated_url = f'{URL}?commodity={commodity_value}&containerall=1'

    soup = load_page(updated_url)

    container_sales = get_daily_container_sales(commodity, soup)

    return container_sales.model_dump()