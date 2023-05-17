import pytest

from cars.tests.factories import CarFactory
from discount.tests.factories import ProviderDiscountFactory, SeasonDiscountFactory
from provider.tests.factories import ProviderFactory
from .factories import CarShowRoomFactory, SellModelFactory


@pytest.fixture()
def create_car_showroom(create_user_car_showroom):
    def car_showroom(**kwargs):
        user = create_user_car_showroom()
        return CarShowRoomFactory(user=user, **kwargs)

    return car_showroom


@pytest.fixture
def build_car_showroom(create_user_car_showroom):
    def car_showroom(**kwargs):
        user = create_user_car_showroom()
        return CarShowRoomFactory.build(user=user, **kwargs)

    return car_showroom


@pytest.fixture()
def create_sell_model(create_user_car_showroom, create_user_provider):
    def sell_model(**kwargs):
        user_car_showroom = create_user_car_showroom()
        user_provider = create_user_provider()
        car_showroom = CarShowRoomFactory(user=user_car_showroom)
        provider = ProviderFactory(user=user_provider)
        return SellModelFactory(
            car=CarFactory(),
            car_showroom=car_showroom,
            provider=provider,
            discount=ProviderDiscountFactory(),
            season_discount=SeasonDiscountFactory(),
            **kwargs
        )

    return sell_model


@pytest.fixture()
def build_sell_model(create_user_car_showroom, create_user_provider):
    def sell_model(**kwargs):
        car = CarFactory()
        discount = ProviderDiscountFactory()
        season_discount = SeasonDiscountFactory()
        user_car_showroom = create_user_car_showroom()
        user_provider = create_user_provider()
        car_showroom = CarShowRoomFactory(user=user_car_showroom)
        provider = ProviderFactory(user=user_provider)
        return SellModelFactory.build(
            car=car,
            car_showroom=car_showroom,
            provider=provider,
            discount=discount,
            season_discount=season_discount,
            **kwargs
        )

    return sell_model
