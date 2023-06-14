import random
from decimal import Decimal

import factory
from factory import fuzzy

from car_showroom.models import CarShowRoom, SellModel
from cars.choice import Color, EngineType, NumberOfDoor, BodyType
from cars.tests.factories import CarFactory
from core.tests.factories import JSONFactory
from discount.tests.factories import ProviderDiscountFactory
from provider.tests.factories import ProviderFactory
from user.tests.factories import UserFactory


class CarShowRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarShowRoom

    name = factory.Faker("name")
    year = factory.Faker("year")
    balance = Decimal("23.99")
    country = random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"])
    list_cars_to_buy = factory.Dict(
        {
            "color": fuzzy.FuzzyChoice(Color),
            "engine_type": fuzzy.FuzzyChoice(EngineType),
            "number_of_doors": fuzzy.FuzzyChoice(NumberOfDoor),
            "body_type": fuzzy.FuzzyChoice(BodyType),
        },
        dict_factory=JSONFactory,
    )

    is_active = True
    user = factory.SubFactory(UserFactory)


class SellModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SellModel

    car_showroom = factory.SubFactory(CarShowRoomFactory)
    car = factory.SubFactory(CarFactory)
    margin = random.randint(0, 100)
    count = random.randint(0, 100)
    provider = factory.SubFactory(ProviderFactory)
    price_provider = Decimal("10.0")


class CarShowRoomWithSellFactory(CarShowRoomFactory):
    Sell = factory.RelatedFactory(SellModelFactory, factory_related_name="sell")
