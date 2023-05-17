import pytest

from car_showroom.tests.factories import CarShowRoomFactory
from customer.tests.factories import TransactionFactory, CustomerFactory
from discount.tests.factories import CarShowRoomDiscountFactory, SeasonDiscountFactory


@pytest.fixture
def build_transaction(create_user_car_showroom):
    def transaction(**kwargs):
        user_car_showroom = create_user_car_showroom()
        car_showroom = CarShowRoomFactory(user=user_car_showroom)
        discount = CarShowRoomDiscountFactory()
        season_discount = SeasonDiscountFactory()
        return TransactionFactory.build(
            car_showroom=car_showroom,
            discount=discount,
            season_discount=season_discount,
        )

    return transaction


@pytest.fixture
def create_transaction(create_user_car_showroom):
    def transaction(**kwargs):
        user_car_showroom = create_user_car_showroom()
        car_showroom = CarShowRoomFactory(user=user_car_showroom)
        return TransactionFactory(
            car_showroom=car_showroom,
            discount=CarShowRoomDiscountFactory(),
            season_discount=SeasonDiscountFactory(),
        )

    return transaction


@pytest.fixture
def build_customer(create_user_customer):
    def customer(**kwargs):
        user = create_user_customer()
        return CustomerFactory.build(
            purchases=TransactionFactory(), user=user, **kwargs
        )

    return customer


@pytest.fixture
def create_customer(create_user_customer):
    def customer(**kwargs):
        user = create_user_customer()
        return CustomerFactory(purchases=TransactionFactory(), user=user, **kwargs)

    return customer
