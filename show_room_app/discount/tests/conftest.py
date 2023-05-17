import pytest

from .factories import (
    CarShowRoomDiscountFactory,
    ProviderDiscountFactory,
    SeasonDiscountFactory,
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
    def provider_discount(**kwargs):
        return CarShowRoomDiscountFactory(**kwargs)

    return provider_discount


@pytest.fixture
def build_car_showroom_discount():
    def provider_discount(**kwargs):
        return CarShowRoomDiscountFactory.build(**kwargs)

    return provider_discount


@pytest.fixture
def create_season_discount():
    def season_discount(**kwargs):
        return SeasonDiscountFactory(**kwargs)

    return season_discount


@pytest.fixture
def build_season_discount():
    def season_discount(**kwargs):
        return SeasonDiscountFactory.build(**kwargs)

    return season_discount
