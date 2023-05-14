import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register


from cars.tests.factories import CarFakeFactory


register(CarFakeFactory)  # car_fake_factory


@pytest.fixture
def api_client():
    client = APIClient()
    return client
