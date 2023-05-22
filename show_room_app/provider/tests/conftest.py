import pytest

from cars.tests.factories import CarFactory
from .factories import ProviderFactory, CarProviderFactory


@pytest.fixture()
def create_provider():
    def provider(**kwargs):
        return ProviderFactory(**kwargs)

    return provider


@pytest.fixture
def build_provider():
    def provider(**kwargs):
        return ProviderFactory.build(**kwargs)

    return provider


@pytest.fixture()
def create_car_provider(create_provider):
    def car_provider(**kwargs):
        return CarProviderFactory(
            car=CarFactory(), provider=create_provider(), **kwargs
        )

    return car_provider


@pytest.fixture()
def build_car_provider():
    def car_provider(**kwargs):
        return CarProviderFactory.build(**kwargs)

    return car_provider
