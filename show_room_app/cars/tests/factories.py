from decimal import Decimal
import random

import factory

from cars.choice import BodyType, Color, EnginType, NumberOfDoor
from cars.models import Car
from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    name = "Opel"
    model_car = "yyy"
    year = 2011
    country = "FR"
    body_type = "Hatchback"
    color = "Victoria"
    engine_type = "Hybrid"
    number_of_doors = "five-door"
    price = Decimal("9.99")
    is_active = True


class CarFakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    name = fake.vehicle_make()
    model_car = fake.vehicle_model()
    image = ""
    year = int(fake.vehicle_year())
    country = random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"])
    body_type = random.choice(BodyType.choices[1])
    color = random.choice(Color.choices[1])
    engine_type = random.choice(EnginType.choices[1])
    number_of_doors = random.choice(NumberOfDoor.choices[1])
    price = Decimal("23.99")
    is_active = True
