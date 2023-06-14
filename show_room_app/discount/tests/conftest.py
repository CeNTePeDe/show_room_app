import pytest

from .factories import (
    CarShowRoomDiscountFactory,
    ProviderDiscountFactory,
)


@pytest.fixture
def create_provider_discount():
    def provider_discount(**kwargs):
        return ProviderDiscountFactory(**kwargs)

    return provider_discount


@pytest.fixture
def build_provider_discount():
    def provider_discount(**kwargs):
        return ProviderDiscountFactory.build(**kwargs)

    return provider_discount


@pytest.fixture
def create_car_showroom_discount():
    def car_showroom_discount(**kwargs):
        return CarShowRoomDiscountFactory(**kwargs)

    return car_showroom_discount


@pytest.fixture
def build_car_showroom_discount():
    def car_showroom_discount(**kwargs):
        return CarShowRoomDiscountFactory.build(**kwargs)

    return car_showroom_discount
