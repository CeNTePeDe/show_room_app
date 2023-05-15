import random

import factory

from discount.models import ProviderDiscount, CarShowRoomDiscount, SeasonDiscount
from faker import Faker

faker = Faker()


class ProviderDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProviderDiscount

    id = factory.Sequence(lambda n: n + 1)
    discount_name = faker.name()
    discount_rate = random.randint(0, 100)


class CarShowRoomDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarShowRoomDiscount

    discount_name = faker.name()
    discount_rate = random.randint(0, 100)


class SeasonDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SeasonDiscount

    id = factory.Sequence(lambda n: n + 1)
    discount_name = faker.name()
    date_start = factory.Faker("date")
    date_finish = factory.Faker("date")
    discount_rate = random.randint(0, 100)
