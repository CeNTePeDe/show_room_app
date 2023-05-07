import random
import pytest
from rest_framework.test import APIClient
from cars.choice import BodyType, EnginType, NumberOfDoor, Color
from faker import Faker
from faker_vehicle import VehicleProvider

from cars.models import Car

fake = Faker()

fake.add_provider(VehicleProvider)


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def car_payload():
    payload = {
        'name': fake.vehicle_make(),
        'model_car': fake.vehicle_model(),
        'image': '',
        'year': fake.vehicle_year(),
        'country': random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"]),
        'body_type': random.choice(BodyType.choices[0]),
        'color': random.choice(Color.choices[0]),
        'engine_type': random.choice(EnginType.choices[0]),
        'number_of_doors': random.choice(NumberOfDoor.choices[0]),
        'price':  str(round(random.uniform(5000.33, 200000.66), 2)),
        'is_active': True,
    }
    return payload

@pytest.fixture
def create_car():
    payload = {
        'name': fake.vehicle_make(),
        'model_car': fake.vehicle_model(),
        'image': '',
        'year': fake.vehicle_year(),
        'country': random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"]),
        'body_type': random.choice(BodyType.choices[1]),
        'color': random.choice(Color.choices[1]),
        'engine_type': random.choice(EnginType.choices[1]),
        'number_of_doors': random.choice(NumberOfDoor.choices[1]),
        'price': str(round(random.uniform(5000.33, 200000.66), 2)),
        'is_active': True,
    }
    record = Car.objects.create(**payload)
    return record

