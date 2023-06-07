import pytest

from cars.tests.factories import CarFactory


@pytest.fixture()
def create_car():
    def car(**kwargs):
        return CarFactory(**kwargs)

    return car


@pytest.fixture()
def build_car():
    def car(**kwargs):
        return CarFactory.build(**kwargs)

    return car
