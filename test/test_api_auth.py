import requests
from django.test import TestCase


class TestApiAuth(TestCase):
    """make a simple get request to product endpoing"""

    url = "http://localhost:8000/api/product"
    response = requests.get(url)
    assert response.status_code == 200
