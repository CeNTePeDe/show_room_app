import random

import pytest

from car_showroom.tests.factories import CarShowRoomFactory, SellModelFactory
from discount.tests.factories import CarShowRoomDiscountFactory


@pytest.fixture()
def create_car_showroom():
    def car_showroom(**kwargs):
        return CarShowRoomFactory(**kwargs)

    return car_showroom


@pytest.fixture
def build_car_showroom():
    def car_showroom(**kwargs):
        return CarShowRoomFactory.build(**kwargs)

    return car_showroom


@pytest.fixture()
def create_sell_model(create_user_car_showroom, create_user_provider):
    def sell_model(**kwargs):
        return SellModelFactory(**kwargs)

    return sell_model


@pytest.fixture()
def build_sell_model():
    def sell_model(**kwargs):
        return SellModelFactory.build(**kwargs)

    return sell_model


@pytest.fixture()
def create_season_discount():
    def season_discount(**kwargs):
        return CarShowRoomDiscountFactory(
            discount_name="season_discount",
            discount_rate=random.randint(0, 100),
            **kwargs
        )

    return season_discount
