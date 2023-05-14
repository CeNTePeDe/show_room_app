import pytest
import json
import requests
from datetime import datetime
from django.urls import reverse
from rest_framework import status
from faker import Faker
from faker_vehicle import VehicleProvider

from cars.models import Car
from cars.tests.factories import CarFakeFactory
from cars.serializer import CarSerializer

ENDPOINT = "/api/v1_car/cars/"
pytestmark = pytest.mark.django_db


def test_car_list(client):
    url = reverse("car-list")
    response = client.get(url)
    car = Car.objects.all()
    expected_data = CarSerializer(car, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


def test_create_car(client):
    car = CarFakeFactory.build()
    expected_json = {
        "name": car.name,
        "model_car": car.model_car,
        "year": car.year,
        "country": car.country.name,
        "body_type": car.body_type,
        "color": car.color,
        "engine_type": car.engine_type,
        "number_of_doors": car.number_of_doors,
        "price": car.price.amount,
        "is_active": car.is_active,
    }
    print("expected_json=", expected_json)
    response = client.post(ENDPOINT, data=expected_json)
    assert response.status_code == 201
    assert json.loads(response.content)["name"] == car.name
    assert json.loads(response.content)["model_car"] == car.model_car
    assert json.loads(response.content)["year"] == car.year
    assert json.loads(response.content)["country"] == car.country
    assert json.loads(response.content)["body_type"] == car.body_type
    assert json.loads(response.content)["engine_type"] == car.engine_type
    assert json.loads(response.content)["number_of_doors"] == car.number_of_doors
    assert json.loads(response.content)["price"] == str(car.price.amount)


def test_retrieve(client):
    car = CarFakeFactory.create()
    url = f"{ENDPOINT}{car.id}/"
    expected_json = {
        "name": car.name,
        "model_car": car.model_car,
        "year": car.year,
        "country": car.country.name,
        "body_type": car.body_type,
        "color": car.color,
        "engine_type": car.engine_type,
        "number_of_doors": car.number_of_doors,
        "price": str(car.price.amount),
        "is_active": car.is_active,
    }
    response = client.get(url)
    assert response.status_code == 200
    assert json.loads(response.content)["name"] == car.name
    assert json.loads(response.content)["model_car"] == car.model_car
    assert json.loads(response.content)["year"] == car.year
    assert json.loads(response.content)["country"] == car.country
    assert json.loads(response.content)["body_type"] == car.body_type
    assert json.loads(response.content)["engine_type"] == car.engine_type
    assert json.loads(response.content)["number_of_doors"] == car.number_of_doors
    assert json.loads(response.content)["price"] == str(car.price.amount)


def test_update(client):
    old_car = CarFakeFactory.create()
    new_car = CarFakeFactory.build()
    new_car = {
        "name": new_car.name,
        "model_car": new_car.model_car,
        "year": new_car.year,
        "country": new_car.country.name,
        "body_type": new_car.body_type,
        "color": new_car.color,
        "engine_type": new_car.engine_type,
        "number_of_doors": new_car.number_of_doors,
        "price": new_car.price.amount,
        "is_active": new_car.is_active,
    }

    url = f"{ENDPOINT}{old_car.id}/"

    response = client.put(url, new_car, format="json")

    assert response.status_code == 200
    assert json.loads(response.content) == new_car
