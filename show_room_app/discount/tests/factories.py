import random

import factory

from discount.models import ProviderDiscount, CarShowRoomDiscount


class ProviderDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProviderDiscount

    id = factory.Sequence(lambda n: n + 1)
    discount_name = factory.Faker("name")
    discount_rate = random.randint(0, 100)


class CarShowRoomDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarShowRoomDiscount

    id = factory.Sequence(lambda n: n + 1)
    discount_name = factory.Faker("name")
    discount_rate = random.randint(0, 100)
