import requests

from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

URL = 'https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

@app.get('/{commodity}')
def get_commodity(commodity: str) -> dict:
    """
    Get information of the specified commodity 
    for the day

    Args:
    commodity (str): The commodity name to display
        latest sales for

    Returns:
    dict
    """

    results = soup.select_one('#right2 p b')
    

    return {'commodity': results.text}