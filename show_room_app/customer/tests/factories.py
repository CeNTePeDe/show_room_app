from decimal import Decimal

import factory

from car_showroom.tests.factories import CarShowRoomFactory
from cars.tests.factories import CarFactory
from customer.models import Customer, Transaction


from discount.tests.factories import CarShowRoomDiscountFactory, SeasonDiscountFactory
from user.tests.factories import UserFactory


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    car_showroom = factory.SubFactory(CarShowRoomFactory)
    car = factory.SubFactory(CarFactory)
    price = Decimal("23.99")
    discount = factory.SubFactory(CarShowRoomDiscountFactory)
    season_discount = factory.SubFactory(SeasonDiscountFactory)


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    username = factory.Faker("name")
    balance = Decimal("23.99")
    max_price = Decimal("5413615.00")
    transaction = factory.SubFactory(TransactionFactory)
    is_active = True
    user = factory.SubFactory(UserFactory)
