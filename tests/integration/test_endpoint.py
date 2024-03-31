import os
import requests

def test_call_endpoint():
    ENDPOINT = os.getenv('BASE_URL')
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
