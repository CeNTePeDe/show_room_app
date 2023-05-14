import random
from decimal import Decimal

import factory

from car_showroom.models import CarShowRoom, SellModel
from faker import Faker

from cars.tests.factories import CarFactory
from discount.tests.factories import ProviderDiscountFactory, SeasonDiscountFactory
from provider.tests.factories import ProviderFactory
from user.tests.factories import UserFactory

faker = Faker()


class CarShowRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarShowRoom

    name = faker.name()
    year = int(faker.year())
    balance = Decimal("23.99")
    country = random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"])
    is_active = True
    user = factory.RelatedFactory(UserFactory, related_name="car_showroom")


class SellModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SellModel

    car = factory.SubFactory(CarFactory)
    car_showroom = factory.SubFactory(CarShowRoomFactory)
    provider = factory.SubFactory(ProviderFactory)
    discount = factory.SubFactory(ProviderDiscountFactory)
    season_discount = factory.SubFactory(SeasonDiscountFactory)
    margin = random.randint(0, 100)
    number_of_car = random.randint(0, 100)
