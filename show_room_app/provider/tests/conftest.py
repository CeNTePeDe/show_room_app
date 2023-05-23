import pytest

from cars.tests.factories import CarFactory
from user.tests.factories import UserFactory
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
            car=CarFactory(), provider=create_provider(user=UserFactory(is_provider=True)), **kwargs
        )

    return car_provider


@pytest.fixture()
def build_car_provider():
    def car_provider(**kwargs):
        return CarProviderFactory.build(car=CarFactory(),
                                        provider=ProviderFactory(user=UserFactory(is_provider=True)),
                                        **kwargs)

    return car_provider
