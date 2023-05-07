import pytest
from faker import Faker
from rest_framework.test import APIClient

client = APIClient()
fake = Faker()


@pytest.mark.django_db
def test_register_user():
    url = '/api/v1_user/create/'
    payload = {
        'email': 'fake_email@email.ru',
        'username': 'fake_user',
        'password': '1111',
        'password_confirm': '1111',
        'is_customer': True,
        'is_provider': False,
        'is_car_showroom': False}
    response = client.post(url, payload)
    data = response.data
    assert payload['email'] == data["email"]
    assert payload['username'] == data["username"]
