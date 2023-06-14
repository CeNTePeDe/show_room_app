import random

import pytest

from discount.tests.factories import ProviderDiscountFactory
from provider.tests.factories import ProviderFactory, CarProviderFactory


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


@pytest.fixture()
def create_first_purchase_discount():
    def first_purchase_discount(**kwargs):
        return ProviderDiscountFactory(
            discount_name="first_purchase_discount",
            discount_rate=random.randint(0, 100),
            **kwargs
        )

    return first_purchase_discount


@pytest.fixture()
def create_regular_customer_discount():
    def regular_customer(**kwargs):
        return ProviderDiscountFactory(
            discount_name="regular_customer",
            discount_rate=random.randint(0, 100),
            **kwargs
        )

    return regular_customer
