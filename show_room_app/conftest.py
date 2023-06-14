import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from user.models import User
from user.tests.factories import UserFactory


@pytest.fixture
def simple_api_client():
    client = APIClient()
    return client


@pytest.fixture()
def admin_api_client():
    # Create an admin user
    user = User.objects.create_superuser(
        username="user", email="admin_user@example.ru", password="1111", is_active=True
    )
    access_token = AccessToken.for_user(user)

    # Create an API client and authenticate with the access token
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + str(access_token))
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
