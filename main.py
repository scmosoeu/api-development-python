import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI

from utils.page_connect_helper import load_page

app = FastAPI()

load_dotenv()
URL = os.getenv('BASE_URL')

@app.get('/{commodity}')
def get_commodity(commodity: str) -> dict:
    """
    Get information of the specified commodity 
    for the day

    Args:
    commodity - The commodity name to display
        latest sales for
    """

    soup = load_page(URL)
    results = soup.select_one('#right2 p b')

    return {'commodity': results.text}