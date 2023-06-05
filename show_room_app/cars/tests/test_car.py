import pytest
import json

from decimal import Decimal
from django.urls import reverse

ENDPOINT = "/api/v1_car/cars/"


@pytest.mark.django_db
def test_car_endpoint(simple_api_client):
    url = reverse("car-list")
    response = simple_api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car(admin_api_client, build_car):
    car = build_car()
    payload = {
        "name": car.name,
        "model_car": car.model_car,
        "year": int(car.year),
        "country": car.country,
        "body_type": car.body_type,
        "color": car.color,
        "engine_type": car.engine_type,
        "number_of_doors": car.number_of_doors,
        "price": car.price.amount,
        "is_active": car.is_active,
    }

    response = admin_api_client.post(ENDPOINT, data=payload)
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
def test_retrieve_car(simple_api_client, create_car):
    car = create_car()
    url = f"{ENDPOINT}{car.id}/"
    payload = {
        "name": car.name,
        "model_car": car.model_car,
        "year": int(car.year),
        "country": car.country,
        "body_type": car.body_type,
        "color": car.color,
        "engine_type": car.engine_type,
        "number_of_doors": car.number_of_doors,
        "price": str(car.price.amount),
        "is_active": car.is_active,
    }

    response = simple_api_client.get(url)
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
def test_update_car(admin_api_client, create_car, build_car):
    create_car = create_car()
    build_car = build_car()
    url = f"{ENDPOINT}{create_car.id}/"

    payload = {
        "name": build_car.name,
        "model_car": build_car.model_car,
        "year": int(build_car.year),
        "country": build_car.country.code,
        "body_type": build_car.body_type,
        "color": build_car.color,
        "engine_type": build_car.engine_type,
        "number_of_doors": build_car.number_of_doors,
        "price": "22.10",
        "is_active": build_car.is_active,
    }

    response = admin_api_client.put(
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
def test_delete_car(admin_api_client, create_car):
    car = create_car()
    url = f"{ENDPOINT}{car.id}/"
    response = admin_api_client.delete(url)

    assert response.status_code == 405
