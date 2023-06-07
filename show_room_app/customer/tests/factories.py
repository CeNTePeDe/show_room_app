from decimal import Decimal

import factory
from faker import Faker
from faker_vehicle import VehicleProvider

from car_showroom.tests.factories import CarShowRoomFactory
from cars.tests.factories import CarFactory
from customer.models import Customer, Transaction
from user.tests.factories import UserFactory

fake = Faker()
fake.add_provider(VehicleProvider)


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    car = factory.SubFactory(CarFactory)
    customer = factory.SubFactory(Customer)
    car_showroom = factory.SubFactory(CarShowRoomFactory)
    price = Decimal("23.99")


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    username = factory.Faker("name")
    balance = Decimal("23.99")
    model_car = factory.Dict(
        {"name": fake.vehicle_make(), "model": fake.vehicle_model(), "price": 0.0}
    )
    is_active = True
    user = factory.SubFactory(UserFactory)
