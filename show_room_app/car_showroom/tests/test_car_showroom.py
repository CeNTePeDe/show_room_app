import json
import pytest
from rest_framework_simplejwt.tokens import AccessToken

ENDPOINT = "/api/v1_car_showroom/car_showroom/"


@pytest.mark.django_db
def test_car_showroom_get_endpoint(simple_api_client):
    response = simple_api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car_showroom(
    simple_api_client,
    build_car_showroom,
    create_user_car_showroom,
):
    user = create_user_car_showroom()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    car_showroom = build_car_showroom(user=user)

    payload = {
        "name": car_showroom.name,
        "year": car_showroom.year,
        "balance": str(car_showroom.balance.amount),
        "country": car_showroom.country.code,
        "list_cars_to_buy": car_showroom.list_cars_to_buy,
        "user": car_showroom.user.id,
        "is_active": car_showroom.is_active,
    }

    response = simple_api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_car_showroom(
    simple_api_client, create_car_showroom, create_user_car_showroom
):
    user = create_user_car_showroom()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    car_showroom = create_car_showroom(user=user)
    url = f"{ENDPOINT}{car_showroom.user.id}/"

    payload = {
        "name": car_showroom.name,
        "year": int(car_showroom.year),
        "balance": car_showroom.balance.amount,
        "country": car_showroom.country.code,
        "list_cars_to_buy": car_showroom.list_cars_to_buy,
        "user": car_showroom.user.id,
        "is_active": car_showroom.is_active,
    }
    response = simple_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["list_cars_to_buy"] == data["list_cars_to_buy"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db
def test_update_car_showroom(
    simple_api_client, create_user_car_showroom, build_car_showroom, create_car_showroom
):
    user = create_user_car_showroom()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    car_showroom = create_car_showroom(user=user)
    build_car_showroom = build_car_showroom()
    payload = {
        "name": build_car_showroom.name,
        "year": int(build_car_showroom.year),
        "country": build_car_showroom.country.code,
        "list_cars_to_buy": build_car_showroom.list_cars_to_buy,
        "balance": str(build_car_showroom.balance.amount),
        "user": car_showroom.user.id,
        "is_active": build_car_showroom.is_active,
    }
    url = f"{ENDPOINT}{car_showroom.user.id}/"
    response = simple_api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["list_cars_to_buy"] == data["list_cars_to_buy"]
    assert payload["is_active"] == data["is_active"]


@pytest.mark.django_db
def test_delete_car_showroom(
    simple_api_client, create_car_showroom, create_user_car_showroom
):
    user = create_user_car_showroom()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    car_showroom = create_car_showroom(user=user)
    url = f"{ENDPOINT}{car_showroom.user.id}/"
    response = simple_api_client.delete(url)

    assert response.status_code == 405
