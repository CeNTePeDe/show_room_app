import pytest
from rest_framework.test import APIClient

from user.tests.factories import UserFactory


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture()
def create_user_customer():
    def user(**kwargs):
        return UserFactory(is_customer=True, **kwargs)

    return user


@pytest.fixture()
def create_user_car_showroom():
    def user(**kwargs):
        return UserFactory(is_car_showroom=True, **kwargs)

    return user


@pytest.fixture()
def create_user_provider():
    def user(**kwargs):
        return UserFactory(is_provider=True, **kwargs)

    return user


@pytest.fixture()
def build_user_customer():
    def user(**kwargs):
        return UserFactory.build(username="customer1", is_customer=True, **kwargs)

    return user


@pytest.fixture()
def build_user_car_showroom():
    def user(**kwargs):
        return UserFactory.build(is_car_showroom=True, **kwargs)

    return user


@pytest.fixture()
def build_user_provider():
    def user(**kwargs):
        return UserFactory.build(username="provider", is_provider=True, **kwargs)

    return user
