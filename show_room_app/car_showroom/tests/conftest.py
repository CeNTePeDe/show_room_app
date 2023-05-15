import pytest

from cars.tests.factories import CarFactory
from discount.tests.factories import ProviderDiscountFactory, SeasonDiscountFactory
from provider.tests.factories import ProviderFactory
from user.tests.factories import UserFactory
from .factories import CarShowRoomFactory, SellModelFactory


@pytest.fixture
def create_car_showroom():
    user = UserFactory()
    create_car_showroom = CarShowRoomFactory.create(user=user)
    return create_car_showroom


@pytest.fixture
def build_car_showroom():
    user = UserFactory()
    build_car_showroom = CarShowRoomFactory.build(user=user)
    return build_car_showroom


@pytest.fixture
def create_sell_model():
    user = UserFactory()
    car = CarFactory()
    car_showroom = CarShowRoomFactory(user=user)
    provider = ProviderFactory(user=user)
    discount = ProviderDiscountFactory()
    season_discount = SeasonDiscountFactory()
    create_sell_model = SellModelFactory.create(car=car, car_showroom=car_showroom,
                                                provider=provider, discount=discount,
                                                season_discount=season_discount)
    return create_sell_model


@pytest.fixture
def build_sell_model():
    car = CarFactory()
    user = UserFactory()
    car_showroom = CarShowRoomFactory(user=user)
    provider = ProviderFactory(user=user)
    discount = ProviderDiscountFactory()
    season_discount = SeasonDiscountFactory()
    build_sell_model = SellModelFactory.build(car=car, car_showroom=car_showroom,
                                              provider=provider, discount=discount,
                                              season_discount=season_discount)
    return build_sell_model
