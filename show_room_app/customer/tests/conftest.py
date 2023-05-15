import pytest

from car_showroom.tests.factories import CarShowRoomFactory
from customer.tests.factories import TransactionFactory, CustomerFactory
from discount.tests.factories import CarShowRoomDiscountFactory, SeasonDiscountFactory
from user.tests.factories import UserFactory


@pytest.fixture
def build_transaction():
    car_showroom = CarShowRoomFactory()
    discount = CarShowRoomDiscountFactory()
    season_discount = SeasonDiscountFactory()
    transaction_build = TransactionFactory.build(
        car_showroom=car_showroom, discount=discount, season_discount=season_discount
    )
    return transaction_build


@pytest.fixture
def create_transaction():
    car_showroom = CarShowRoomFactory()
    discount = CarShowRoomDiscountFactory()
    season_discount = SeasonDiscountFactory()
    transaction_create = TransactionFactory.create(
        car_showroom=car_showroom, discount=discount, season_discount=season_discount
    )
    return transaction_create


@pytest.fixture
def build_customer():
    user = UserFactory()
    purchases = TransactionFactory()
    build_customer = CustomerFactory.build(purchases=purchases, user=user)
    return build_customer


@pytest.fixture
def create_customer():
    user_car_showroom = UserFactory()
    car_showroom = CarShowRoomFactory(user=user_car_showroom)
    user_customer = UserFactory()
    discount = CarShowRoomDiscountFactory()
    season_discount = SeasonDiscountFactory()
    purchases = TransactionFactory(car_showroom=car_showroom, discount=discount, season_discount=season_discount)
    create_customer = CustomerFactory.create(purchases=purchases, user=user_customer)
    return create_customer
