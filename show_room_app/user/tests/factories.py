import factory

from user.models import User
from faker import Faker

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "john%s" % n)
    email = faker.email()
    first_name = faker.first_name()
    last_name = faker.last_name()
    password = "1111"
    password_confirm = "1111"
    is_customer = False
    is_provider = False
    is_car_showroom = False
