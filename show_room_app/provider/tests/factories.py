import random

import factory

from cars.tests.factories import CarFactory
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
    is_active = True
    user = factory.RelatedFactory(UserFactory, related_name="provider")


class CarProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarProvider

    car = factory.SubFactory(CarFactory)
    provider = factory.SubFactory(ProviderFactory)
    margin = random.randint(0, 100)
    number_of_car = random.randint(0, 100)
