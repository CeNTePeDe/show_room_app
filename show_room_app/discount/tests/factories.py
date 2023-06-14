import random

import factory

from discount.models import ProviderDiscount, CarShowRoomDiscount


class ProviderDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProviderDiscount

    id = factory.Sequence(lambda n: n + 1)
    discount_name = factory.Faker("name")
    discount_rate = random.randint(0, 100)
    date_start = factory.Faker("date_between", start_date="-1y", end_date="today")
    date_finish = factory.Faker("date_between", start_date=date_start, end_date="+1y")
    special_discount = True
    is_active = True


class CarShowRoomDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarShowRoomDiscount

    id = factory.Sequence(lambda n: n + 1)
    discount_name = factory.Faker("name")
    discount_rate = random.randint(0, 100)
    date_start = factory.Faker("date_between", start_date="-1y", end_date="today")
    date_finish = factory.Faker("date_between", start_date=date_start, end_date="+1y")
    special_discount = True
    is_active = True
