import pytest

from cars.tests.factories import CarFactory
from discount.tests.factories import ProviderDiscountFactory
from provider.tests.factories import ProviderFactory
from .factories import CarShowRoomFactory, SellModelFactory


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
        return SellModelFactory(
            car=CarFactory(),
            car_showroom=CarShowRoomFactory(user=create_user_car_showroom()),
            provider=ProviderFactory(user=create_user_provider),
            discount=ProviderDiscountFactory(),
            **kwargs
        )

    return sell_model


@pytest.fixture()
def build_sell_model(create_user_car_showroom, create_user_provider):
    def sell_model(**kwargs):
        return SellModelFactory.build(
            car=CarFactory(),
            car_showroom=CarShowRoomFactory(user=create_user_car_showroom()),
            provider=ProviderFactory(user=create_user_provider()),
            discount=ProviderDiscountFactory(),
            **kwargs
        )

    return sell_model
