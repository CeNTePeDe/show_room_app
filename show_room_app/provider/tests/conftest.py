import pytest

from cars.tests.factories import CarFactory
from user.tests.factories import UserFactory
from .factories import ProviderFactory, CarProviderFactory


@pytest.fixture
def create_provider():
    user = UserFactory()
    create_provider = ProviderFactory.create(user=user)
    return create_provider


@pytest.fixture
def build_provider():
    user = UserFactory()
    build_provider = ProviderFactory.build(user=user)
    return build_provider


@pytest.fixture
def create_car_provider():
    provider = ProviderFactory()
    car = CarFactory()
    create_car_provider = CarProviderFactory.create(car=car, provider=provider)
    return create_car_provider


@pytest.fixture
def build_car_provider():
    provider = ProviderFactory()
    car = CarFactory()
    build_car_provider = CarProviderFactory.build(car=car, provider=provider)
    return build_car_provider
