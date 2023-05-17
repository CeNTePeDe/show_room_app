import pytest

from cars.tests.factories import CarFactory
from .factories import ProviderFactory, CarProviderFactory


@pytest.fixture()
def create_provider(create_user_provider):
    def provider(**kwargs):
        return ProviderFactory(user=create_user_provider(), **kwargs)

    return provider


@pytest.fixture
def build_provider(create_user_provider):
    def provider(**kwargs):
        return ProviderFactory.build(user=create_user_provider(), **kwargs)

    return provider


@pytest.fixture()
def create_car_provider(create_provider):
    def car_provider(**kwargs):
        return CarProviderFactory(
            car=CarFactory(), provider=create_provider(), **kwargs
        )

    return car_provider


@pytest.fixture()
def build_car_provider(create_provider):
    def car_provider(**kwargs):
        return CarProviderFactory.build(
            car=CarFactory(), provider=create_provider(), **kwargs
        )

    return car_provider
