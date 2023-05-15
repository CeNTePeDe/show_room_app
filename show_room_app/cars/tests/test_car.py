import pytest
import json

from decimal import Decimal
from django.urls import reverse

from cars.models import Car
from cars.tests.factories import CarFactory
from cars.serializer import CarSerializer

ENDPOINT = "/api/v1_car/cars/"


@pytest.mark.django_db
def test_car_list(client):
    url = reverse("car-list")
    response = client.get(url)
    car = Car.objects.all()
    expected_data = CarSerializer(car, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_car(client, build_car):
    payload = {
        "name": build_car.name,
        "model_car": build_car.model_car,
        "year": build_car.year,
        "country": build_car.country,
        "body_type": build_car.body_type,
        "color": build_car.color,
        "engine_type": build_car.engine_type,
        "number_of_doors": build_car.number_of_doors,
        "price": build_car.price.amount,
        "is_active": build_car.is_active,
    }
    response = client.post(ENDPOINT, data=payload)
    data = response.data
    assert response.status_code == 201
    assert payload["name"] == data["name"]
    assert payload["model_car"] == data["model_car"]
    assert payload["year"] == data["year"]
    assert payload["country"] == data["country"]
    assert payload["body_type"] == data["body_type"]
    assert payload["engine_type"] == data["engine_type"]
    assert payload["number_of_doors"] == data["number_of_doors"]
    assert payload["price"] == Decimal(data["price"])
    assert payload["is_active"] == data["is_active"]


@pytest.mark.django_db
def test_retrieve_car(client, create_car):
    url = f"{ENDPOINT}{create_car.id}/"
    payload = {
        "name": create_car.name,
        "model_car": create_car.model_car,
        "year": create_car.year,
        "country": create_car.country,
        "body_type": create_car.body_type,
        "color": create_car.color,
        "engine_type": create_car.engine_type,
        "number_of_doors": create_car.number_of_doors,
        "price": str(create_car.price.amount),
        "is_active": create_car.is_active,
    }
    response = client.get(url)
    data = response.data
    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["model_car"] == data["model_car"]
    assert payload["year"] == data["year"]
    assert payload["country"] == data["country"]
    assert payload["body_type"] == data["body_type"]
    assert payload["engine_type"] == data["engine_type"]
    assert payload["number_of_doors"] == data["number_of_doors"]
    assert payload["price"] == data["price"]
    assert payload["is_active"] == data["is_active"]


@pytest.mark.django_db
def test_update_car(client, create_car, build_car):
    url = f"{ENDPOINT}{create_car.id}/"

    payload = {
        "name": build_car.name,
        "model_car": build_car.model_car,
        "year": build_car.year,
        "country": build_car.country.code,
        "body_type": build_car.body_type,
        "color": build_car.color,
        "engine_type": build_car.engine_type,
        "number_of_doors": build_car.number_of_doors,
        "price": "22.10",
        "is_active": build_car.is_active,
    }

    response = client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["model_car"] == data["model_car"]
    assert payload["year"] == data["year"]
    assert payload["country"] == data["country"]
    assert payload["body_type"] == data["body_type"]
    assert payload["engine_type"] == data["engine_type"]
    assert payload["number_of_doors"] == data["number_of_doors"]
    assert payload["price"] == data["price"]
    assert payload["is_active"] == data["is_active"]


@pytest.mark.django_db
def test_delete_car(client, create_car):
    url = f"{ENDPOINT}{create_car.id}/"
    response = client.delete(url)
    assert response.status_code == 405