import json
import random

import factory

from cars.tests.factories import CarFactory
from core.default_value import jsonfield_default_value
from core.tests.factories import JSONFactory
from provider.models import Provider, CarProvider
from faker import Faker

from user.tests.factories import UserFactory

faker = Faker()


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider

    name = faker.name()
    year = int(faker.year())
    country = random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"])
    characteristic = factory.Dict({}, dict_factory=JSONFactory)
    is_active = True
    user = factory.SubFactory(UserFactory)


class CarProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarProvider

    car = factory.SubFactory(CarFactory)
    provider = factory.SubFactory(ProviderFactory)
    margin = random.randint(0, 100)
    number_of_cars = random.randint(0, 100)


class ProviderWithCarFactory(ProviderFactory):
    car_provider = factory.RelatedFactory(
        CarProviderFactory, factory_related_name="provider"
    )
