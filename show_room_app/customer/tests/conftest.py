import pytest

from car_showroom.tests.factories import CarShowRoomFactory
from cars.tests.factories import CarFactory
from customer.tests.factories import TransactionFactory, CustomerFactory
from discount.tests.factories import CarShowRoomDiscountFactory, SeasonDiscountFactory
from user.tests.factories import UserFactory


@pytest.fixture
def build_transaction(create_user_car_showroom, create_user_customer):
    def transaction(**kwargs):
        return TransactionFactory.build(
            car=CarFactory(),
            car_showroom=CarShowRoomFactory(user=UserFactory(is_car_showroom=True)),
            discount=CarShowRoomDiscountFactory(),
            season_discount=SeasonDiscountFactory(),
            **kwargs
        )

    return transaction


@pytest.fixture
def create_transaction(create_user_car_showroom, create_user_customer):
    def transaction(**kwargs):
        return TransactionFactory(
            car=CarFactory(),
            car_showroom=CarShowRoomFactory(user=create_user_car_showroom()),
            discount=CarShowRoomDiscountFactory(),
            season_discount=SeasonDiscountFactory(),
            **kwargs
        )

    return transaction


@pytest.fixture
def build_customer():
    def customer(**kwargs):
        return CustomerFactory.build(**kwargs)

    return customer


@pytest.fixture
def create_customer():
    def customer(**kwargs):
        return CustomerFactory(**kwargs)

    return customer
