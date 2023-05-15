import pytest
from .factories import CarFactory


@pytest.fixture
def create_car():
    create_car = CarFactory.create()
    return create_car


@pytest.fixture
def build_car():
    build_car = CarFactory.build()
    return build_car
