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
        username="admin", email="admin@example.com", password="password"
    )

    # Generate an access token for the user
    access_token = AccessToken.for_user(user)

    # Create an API client and authenticate with the access token
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + str(access_token))
    return client


@pytest.fixture()
def customer_api_client():
    # Create a customer user
    user = User.objects.create_user(
        username="user_customer",
        email="user_customer@example.com",
        password="password",
        password_confirm="password",
        is_customer=True,
        is_car_showroom=False,
        is_provider=False,
    )

    # Generate an access token for the customer
    access_token = AccessToken.for_user(user)

    # Create an API client and authenticate with the access token
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + str(access_token))

    return client


@pytest.fixture()
def car_showroom_api_client():
    # Create a car_showroom user
    user = User.objects.create_user(
        username="user_car_showroom",
        email="user_car_showroom@example.com",
        password="password",
        password_confirm="password",
        is_customer=False,
        is_car_showroom=True,
        is_provider=False,
    )

    # Generate an access token for the car_showroom
    access_token = AccessToken.for_user(user)

    # Create an API client and authenticate with the access token
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + str(access_token))

    return client


@pytest.fixture()
def provider_api_client():
    # Create a provider user
    user = User.objects.create_user(
        username="user_provider",
        email="user_provider@example.com",
        password="password",
        password_confirm="password",
        is_customer=False,
        is_car_showroom=False,
        is_provider=True,
    )

    # Generate an access token for the provider
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
