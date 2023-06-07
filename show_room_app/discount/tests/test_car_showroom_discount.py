import pytest
import json

from rest_framework_simplejwt.tokens import AccessToken

from car_showroom.tests.factories import CarShowRoomFactory
from discount.models import CarShowRoomDiscount

ENDPOINT = "/api/v1_discount/car_showroom_discount/"


@pytest.mark.django_db
def test_car_showroom_discount_endpoint(simple_api_client):
    response = simple_api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car_showroom_discount(
    simple_api_client, build_car_showroom_discount, create_user_car_showroom
):
    user = create_user_car_showroom()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    car_showroom = CarShowRoomFactory(user=user)
    car_showroom_discount = build_car_showroom_discount(
        car_showroom_discount=car_showroom
    )

    payload = {
        "discount_name": car_showroom_discount.discount_name,
        "discount_rate": car_showroom_discount.discount_rate,
        "date_start": car_showroom_discount.date_start,
        "date_finish": car_showroom_discount.date_finish,
        "special_discount": True,
        "is_active": True,
        "car_showroom_discount": car_showroom_discount.car_showroom_discount.user.id,
    }

    response = simple_api_client.post(ENDPOINT, data=payload)
    data = response.data

    assert response.status_code == 201
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]


@pytest.mark.django_db
def test_retrieve_car_showroom_discount(
    simple_api_client, create_car_showroom_discount, create_user_car_showroom
):
    user = create_user_car_showroom()
    car_showroom = CarShowRoomFactory(user=user)
    car_showroom_discount = create_car_showroom_discount(
        car_showroom_discount=car_showroom
    )
    url = f"{ENDPOINT}{car_showroom_discount.id}/"

    payload = {
        "discount_name": car_showroom_discount.discount_name,
        "discount_rate": car_showroom_discount.discount_rate,
        "date_start": car_showroom_discount.date_start.strftime("%Y-%m-%d"),
        "date_finish": car_showroom_discount.date_finish.strftime("%Y-%m-%d"),
        "special_discount": True,
        "is_active": True,
        "car_showroom_discount": car_showroom_discount.car_showroom_discount.user.id,
    }
    response = simple_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]
    assert data["date_start"] == payload["date_start"]
    assert data["date_finish"] == payload["date_finish"]
    assert data["car_showroom_discount"] == payload["car_showroom_discount"]


@pytest.mark.django_db
def test_update_car_showroom_discount(
    simple_api_client,
    create_car_showroom_discount,
    build_car_showroom_discount,
    create_user_car_showroom,
):
    user = create_user_car_showroom()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    car_showroom = CarShowRoomFactory(user=user)

    car_showroom_discount = create_car_showroom_discount(
        car_showroom_discount=car_showroom
    )
    build_car_showroom_discount = build_car_showroom_discount()
    payload = {
        "discount_name": build_car_showroom_discount.discount_name,
        "discount_rate": build_car_showroom_discount.discount_rate,
        "date_start": build_car_showroom_discount.date_start.strftime("%Y-%m-%d"),
        "date_finish": build_car_showroom_discount.date_finish.strftime("%Y-%m-%d"),
        "special_discount": True,
        "is_active": True,
        "car_showroom_discount": car_showroom_discount.car_showroom_discount.user.id,
    }
    url = f"{ENDPOINT}{car_showroom_discount.id}/"
    response = simple_api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]
    assert data["date_start"] == payload["date_start"]
    assert data["date_finish"] == payload["date_finish"]
    assert data["car_showroom_discount"] == payload["car_showroom_discount"]


@pytest.mark.django_db
def test_delete_car_showroom_discount(
    simple_api_client, create_car_showroom_discount, create_user_car_showroom
):
    user = create_user_car_showroom()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    car_showroom = CarShowRoomFactory(user=user)
    car_showroom_discount = create_car_showroom_discount(
        car_showroom_discount=car_showroom
    )
    url = f"{ENDPOINT}{car_showroom_discount.id}/"
    response = simple_api_client.delete(url)

    assert response.status_code == 405
    assert CarShowRoomDiscount.objects.all().count() == 1
