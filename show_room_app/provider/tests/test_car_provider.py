import json

import pytest
from rest_framework_simplejwt.tokens import AccessToken

from cars.tests.factories import CarFactory

ENDPOINT = "/api/v1_provider/car_provider/"


@pytest.mark.django_db
def test_car_provider_get_endpoint(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car_provider(
    simple_api_client, create_user_provider, build_car_provider, create_provider
):
    user = create_user_provider()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    provider = create_provider(user=user)
    car = CarFactory.build()
    car_provider = build_car_provider(provider=provider, car=car)
    payload = {
        "car": {
            "name": car_provider.car.name,
            "model_car": car_provider.car.model_car,
            "year": car_provider.car.year,
            "country": car_provider.car.country.code,
            "body_type": car_provider.car.body_type,
            "color": car_provider.car.color,
            "engin_type": car_provider.car.engine_type,
            "number_of_doors": car_provider.car.number_of_doors,
            "price": str(car_provider.car.price.amount),
            "is_active": car_provider.car.is_active,
        },
        "provider": car_provider.provider.name,
        "margin": car_provider.margin,
    }

    response = simple_api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_car_provider(
    simple_api_client, create_user_provider, create_provider, create_car_provider
):
    user = create_user_provider()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))

    provider = create_provider(user=user)
    car = CarFactory.create()
    car_provider = create_car_provider(car=car, provider=provider)

    url = f"{ENDPOINT}{car_provider.id}/"
    payload = {
        "car": {
            "name": car_provider.car.name,
            "model_car": car_provider.car.model_car,
            "year": int(car_provider.car.year),
            "country": car_provider.car.country.code,
            "body_type": car_provider.car.body_type,
            "color": car_provider.car.color,
            "engin_type": car_provider.car.engine_type,
            "number_of_doors": car_provider.car.number_of_doors,
            "price": str(car_provider.car.price.amount),
            "is_active": car_provider.car.is_active,
        },
        "provider": car_provider.provider.name,
        "margin": car_provider.margin,
    }
    response = simple_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["car"]["name"] == data["car"]["name"]
    assert payload["car"]["model_car"] == data["car"]["model_car"]
    assert payload["provider"] == data["provider"]
    assert payload["margin"] == data["margin"]


@pytest.mark.django_db
def test_update_car_provider(
    simple_api_client,
    create_user_provider,
    create_provider,
    create_car_provider,
    build_car_provider,
):
    user = create_user_provider()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))

    provider = create_provider(user=user)
    car = CarFactory.create()

    car_provider = create_car_provider(car=car, provider=provider)
    url = f"{ENDPOINT}{car_provider.id}/"
    car = CarFactory.build()
    new_car_provider = build_car_provider(car=car, provider=provider)
    payload = {
        "car": {
            "name": new_car_provider.car.name,
            "model_car": new_car_provider.car.model_car,
            "year": int(new_car_provider.car.year),
            "country": new_car_provider.car.country.code,
            "body_type": new_car_provider.car.body_type,
            "color": new_car_provider.car.color,
            "engin_type": new_car_provider.car.engine_type,
            "number_of_doors": new_car_provider.car.number_of_doors,
            "price": str(new_car_provider.car.price.amount),
            "is_active": new_car_provider.car.is_active,
        },
        "provider": car_provider.provider.name,
        "margin": new_car_provider.margin,
    }
    response = simple_api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 200
    assert payload["car"]["name"] == data["car"]["name"]
    assert payload["car"]["model_car"] == data["car"]["model_car"]
    assert payload["car"]["body_type"] == data["car"]["body_type"]
    assert payload["provider"] == data["provider"]
    assert payload["margin"] == data["margin"]


@pytest.mark.django_db
def test_delete_car_provider(simple_api_client, create_car_provider):
    car_provider = create_car_provider()
    url = f"{ENDPOINT}{car_provider.id}/"
    response = simple_api_client.delete(url)

    assert response.status_code == 204
