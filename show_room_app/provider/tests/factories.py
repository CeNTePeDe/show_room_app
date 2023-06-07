import random

import factory
from factory import fuzzy

from cars.choice import Color, EngineType, NumberOfDoor, BodyType
from cars.tests.factories import CarFactory
from provider.models import Provider, CarProvider


from user.tests.factories import UserFactory


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider

    name = factory.Faker("name")
    year = factory.Faker("year")
    country = random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"])
    is_active = True
    user = factory.SubFactory(UserFactory)


class CarProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarProvider

    car = factory.SubFactory(CarFactory)
    provider = factory.SubFactory(ProviderFactory)
    margin = random.randint(0, 100)
