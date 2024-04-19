import requests

from bs4 import BeautifulSoup


def load_page(url: str) -> BeautifulSoup:
    """
    Load HTML page for scrapping

    Args:
    url - The url of the page to be scrapped
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup
