import pytest

from .factories import (
    CarShowRoomDiscountFactory,
    ProviderDiscountFactory,
    SeasonDiscountFactory,
)


@pytest.fixture
def create_provider_discount():
    create_provider_discount = ProviderDiscountFactory.create()
    return create_provider_discount


@pytest.fixture
def build_provider_discount():
    build_provider_discount = ProviderDiscountFactory.build()
    return build_provider_discount


@pytest.fixture
def create_car_showroom_discount():
    create_provider_discount = CarShowRoomDiscountFactory.create()
    return create_provider_discount


@pytest.fixture
def build_car_showroom_discount():
    build_provider_discount = CarShowRoomDiscountFactory.build()
    return build_provider_discount


@pytest.fixture
def create_season_discount():
    create_season_discount = SeasonDiscountFactory.create()
    return create_season_discount


@pytest.fixture
def build_season_discount():
    build_season_discount = SeasonDiscountFactory.build()
    return build_season_discount
