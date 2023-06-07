from datetime import date

import pytest
import json
from rest_framework_simplejwt.tokens import AccessToken

from car_showroom.tests.factories import CarShowRoomFactory, SellModelFactory
from cars.tests.factories import CarFactory
from provider.tests.factories import ProviderFactory

ENDPOINT = "/api/v1_car_showroom/sell_car/"


@pytest.mark.django_db
def test_sell_model_get_endpoint(simple_api_client):
    response = simple_api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_sell_model(
    simple_api_client,
    create_user_provider,
    create_user_car_showroom,
    build_sell_model,
    create_car_showroom,
):
    user_car_showroom = create_user_car_showroom()
    user_provider = create_user_provider()
    car_showroom = create_car_showroom(user=user_car_showroom)
    provider = ProviderFactory(user=user_provider)
    car = CarFactory.build()
    sell_model = build_sell_model(car_showroom=car_showroom, car=car, provider=provider)

    payload = {
        "car_showroom": car_showroom.name,
        "car": {
            "name": car.name,
            "model_car": car.model_car,
            "year": car.year,
            "country": car.country.code,
            "body_type": car.body_type,
            "color": car.color,
            "engin_type": car.engine_type,
            "number_of_doors": car.number_of_doors,
            "price": str(car.price.amount),
            "is_active": car.is_active,
        },
        "provider": provider.name,
        "margin": sell_model.margin,
        "date": date.today().strftime("%Y-%m-%d"),
        "count": sell_model.count,
        "price_provider": str(sell_model.price_provider.amount),
    }
    response = simple_api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_sell_model(
    simple_api_client,
    create_sell_model,
    create_user_provider,
    create_user_car_showroom,
):
    user_provider = create_user_provider()
    user_car_showroom = create_user_car_showroom()
    car_showroom = CarShowRoomFactory(user=user_car_showroom)
    provider = ProviderFactory(user=user_provider)
    car = CarFactory()
    sell_model = create_sell_model(
        car=car, car_showroom=car_showroom, provider=provider
    )
    url = f"{ENDPOINT}{sell_model.id}/"

    payload = {
        "car_showroom": car_showroom.name,
        "car": {
            "name": sell_model.car.name,
            "model_car": sell_model.car.model_car,
            "year": sell_model.car.year,
            "country": sell_model.car.country.code,
            "body_type": sell_model.car.body_type,
            "color": sell_model.car.color,
            "engin_type": sell_model.car.engine_type,
            "number_of_doors": sell_model.car.number_of_doors,
            "price": str(sell_model.car.price.amount),
            "is_active": sell_model.car.is_active,
        },
        "provider": sell_model.provider.name,
        "margin": sell_model.margin,
        "date": date.today().strftime("%Y-%m-%d"),
        "count": sell_model.count,
        "price_provider": str(sell_model.price_provider.amount),
    }

    response = simple_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["car"]["name"] == data["car"]["name"]
    assert payload["car_showroom"] == data["car_showroom"]
    assert payload["provider"] == data["provider"]
    assert payload["margin"] == data["margin"]


@pytest.mark.django_db
def test_delete_sell_model(
    simple_api_client, create_sell_model, create_user_provider, create_user_car_showroom
):
    user_provider = create_user_provider()
    user_car_showroom = create_user_car_showroom()
    car_showroom = CarShowRoomFactory(user=user_car_showroom)
    provider = ProviderFactory(user=user_provider)
    car = CarFactory()
    sell_model = create_sell_model(
        car=car, car_showroom=car_showroom, provider=provider
    )
    url = f"{ENDPOINT}{sell_model.id}/"
    response = simple_api_client.delete(url)

    assert response.status_code == 405
