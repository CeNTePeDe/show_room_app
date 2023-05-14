import factory

from user.models import User
from faker import Faker

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = faker.name()
    email = faker.email()
    first_name = faker.first_name()
    last_name = faker.last_name()
    is_customer = False
    is_provider = False
    is_car_showroom = False


class UserCustomerFactory(UserFactory):
    is_customer = True


class UserProviderFactory(UserFactory):
    is_provider = True


class UserCarShowRoomFactory(UserFactory):
    is_car_showroom = True
