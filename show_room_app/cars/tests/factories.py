from decimal import Decimal
import random

import factory
from factory import fuzzy

from cars.choice import BodyType, Color, EnginType, NumberOfDoor
from cars.models import Car
from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    id = factory.Sequence(lambda n: n + 1)
    name = fake.vehicle_make()
    model_car = fake.vehicle_model()
    image = ""
    year = int(fake.vehicle_year())
    country = random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"])
    body_type = fuzzy.FuzzyChoice(BodyType)
    color = fuzzy.FuzzyChoice(Color)
    engine_type = fuzzy.FuzzyChoice(EnginType)
    number_of_doors = fuzzy.FuzzyChoice(NumberOfDoor)
    price = "23.99"
    is_active = True
