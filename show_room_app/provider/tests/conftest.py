import random

import pytest

from cars.tests.factories import CarFactory
from discount.tests.factories import ProviderDiscountFactory
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
        return CarProviderFactory(**kwargs)

    return car_provider


@pytest.fixture()
def build_car_provider():
    def car_provider(**kwargs):
        return CarProviderFactory.build(**kwargs)

    return car_provider


@pytest.fixture()
def create_season_discount():
    def season_discount(**kwargs):
        return ProviderDiscountFactory(
            discount_name="season_discount",
            discount_rate=random.randint(0, 100),
            **kwargs
        )

    return season_discount
