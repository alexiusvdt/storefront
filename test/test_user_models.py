# import factory
# import pytest
import requests
from django.test import TestCase
from faker import Faker
from rest_framework.authtoken.models import Token

# from user.models import User

fake = Faker()


class TestUserCreate(TestCase):
    def test_create_user(self):
        """attempts to create a basic user account"""
        url = "http://127.0.0.1:8000/api/users/"
        email = fake.email()
        data = {
            "username": email,
            "password": "hotbologna",
            "email": email,
            "first_name": "Tim",
            "last_name": "tom",
            "phone_no": 50345348,
            "is_employee": False,
        }
        # double check this corresponds to viewsets and not written for APIView!
        response = requests.post(url, data=data)
        if response.status_code == 201:
            assert response.status_code == 201
        else:
            print("Error: {0}".format(response.status_code), response)
            assert response.status_code == 201


class TestUserUpdate(TestCase):
    def test_update_user(self):
        """PUT data to an existing user record"""
        url = "http://127.0.0.1:8000/api/users/1/"
        data = {"first_name": "Updated"}
        response = requests.patch(url, data=data)
        if response.status_code == 200:
            assert response.status_code == 200
        else:
            print("Error: {0}".format(response.status_code))
            assert response.status_code == 200


class TestUserGetAll(TestCase):
    def test_get_list_of_users(self):
        """GET all users in DB"""
        url = "http://127.0.0.1:8000/api/users"
        response = requests.get(url)
        assert response.status_code == 200
