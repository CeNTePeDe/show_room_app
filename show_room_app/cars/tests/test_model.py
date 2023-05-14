import pytest
from decimal import Decimal
from pytest_factoryboy import register

from cars.tests.factories import CarFactory

register(CarFactory)
pytestmark = pytest.mark.django_db


def test_model_fixture(car):
    assert car.name == "Opel"
    assert car.model_car == "yyy"
    assert car.year == 2011
    assert car.country == "FR"
    assert car.body_type == "Hatchback"
    assert car.color == "Victoria"
    assert car.engine_type == "Hybrid"
    assert car.number_of_doors == "five-door"
    assert car.price.amount == Decimal("9.99")
    assert car.is_active == True
