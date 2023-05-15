import pytest
import json

from cars.tests.factories import CarFactory
from provider.tests.factories import (
    ProviderFactory,
    CarProviderFactory,
)

ENDPOINT = "/api/v1_provider/car_provider/"


@pytest.mark.django_db
def test_car_provider_get_endpoint(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car_provider(client, build_car_provider):
    payload = {
        "car": build_car_provider.car.id,
        "provider": build_car_provider.provider.user.id,
        "margin": build_car_provider.margin,
        "number_of_cars": build_car_provider.number_of_cars,
    }
    response = client.post(ENDPOINT, data=payload)
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_car_provider(client, create_car_provider):
    url = f"{ENDPOINT}{create_car_provider.id}/"
    payload = {
        "car": create_car_provider.car.id,
        "provider": create_car_provider.provider.user.id,
        "margin": create_car_provider.margin,
        "number_of_cars": create_car_provider.number_of_cars,
    }
    response = client.get(url)
    data = response.data
    assert response.status_code == 200
    assert payload["car"] == data["car"]
    assert payload["provider"] == data["provider"]
    assert payload["margin"] == data["margin"]
    assert payload["number_of_cars"] == data["number_of_cars"]


@pytest.mark.django_db
def test_update_car_provider(client):
    provider = ProviderFactory()
    car = CarFactory()
    old_car_provider = CarProviderFactory.create(car=car, provider=provider)
    new_car_provider = CarProviderFactory.build(car=car, provider=provider)
    url = f"{ENDPOINT}{old_car_provider.id}/"
    payload = {
        "car": new_car_provider.car.id,
        "provider": new_car_provider.provider.user.id,
        "margin": new_car_provider.margin,
        "number_of_cars": new_car_provider.number_of_cars,
    }
    response = client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert payload["car"] == data["car"]
    assert payload["provider"] == data["provider"]
    assert payload["margin"] == data["margin"]
    assert payload["number_of_cars"] == data["number_of_cars"]
