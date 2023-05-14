from decimal import Decimal

import factory

from car_showroom.tests.factories import CarShowRoomFactory
from customer.models import Customer, Transaction
from faker import Faker

from discount.tests.factories import CarShowRoomDiscountFactory, SeasonDiscountFactory
from user.tests.factories import UserFactory

faker = Faker()


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    car_showroom = factory.SubFactory(CarShowRoomFactory)
    price = Decimal("23.99")
    discount = factory.SubFactory(CarShowRoomDiscountFactory)
    season_discount = factory.SubFactory(SeasonDiscountFactory)


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    username = faker.name()
    balance = Decimal("23.99")
    purchase = factory.SubFactory(TransactionFactory)
    max_price = Decimal("5413615.00")
    is_active = True
    user = factory.RelatedFactory(UserFactory, related_name="customer")
