from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_commodity_sales_200():

    response = client.get('/apples')

    assert response.status_code == 200


def test_commodity_sales_404():

    response = client.get('/fresh_produce')

    assert response.status_code == 404


def test_container_sales_200():

    response = client.get('containers/pears')

    assert response.status_code == 200


def test_container_sales_404():

    response = client.get('containers/some_product')

    assert response.status_code == 404