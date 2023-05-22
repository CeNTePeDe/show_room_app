import pytest

from car_showroom.tests.factories import CarShowRoomFactory
from customer.tests.factories import TransactionFactory, CustomerFactory
from discount.tests.factories import CarShowRoomDiscountFactory, SeasonDiscountFactory


@pytest.fixture
def build_transaction(create_user_car_showroom, create_user_customer):
    def transaction(**kwargs):
        user_car_showroom = create_user_car_showroom()
        user_customer = create_user_customer()

        return TransactionFactory.build(
            customer=CustomerFactory(user=user_customer),
            car_showroom=CarShowRoomFactory(user=user_car_showroom),
            discount=CarShowRoomDiscountFactory(),
            season_discount=SeasonDiscountFactory(),
            **kwargs
        )

    return transaction


@pytest.fixture
def create_transaction(create_user_car_showroom, create_user_customer):
    def transaction(**kwargs):
        user_car_showroom = create_user_car_showroom()
        car_showroom = CarShowRoomFactory(user=user_car_showroom)
        return TransactionFactory(
            car_showroom=car_showroom,
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
