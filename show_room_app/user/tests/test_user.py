import json

import pytest
from django.urls import reverse


ENDPOINT = "/api/v1_user/register/"


@pytest.mark.django_db
def test_user_endpoint(client):
    url = reverse("user-list")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user_customer(client, build_user_customer):
    user = build_user_customer()
    payload = {
        "username": user.username,
        "password": "1111",
        "password_confirm": "1111",
        "email": user.email,
        "is_customer": user.is_customer,
        "is_provider": user.is_provider,
        "is_car_showroom": user.is_car_showroom,
    }
    response = client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 201
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert data["is_customer"] == payload["is_customer"]
    assert data["is_provider"] == payload["is_provider"]
    assert data["is_car_showroom"] == payload["is_car_showroom"]


@pytest.mark.django_db
def test_create_user_car_showroom(client, build_user_car_showroom):
    user = build_user_car_showroom()
    payload = {
        "username": user.username,
        "password": "1111",
        "password_confirm": "1111",
        "email": user.email,
        "is_customer": user.is_customer,
        "is_provider": user.is_provider,
        "is_car_showroom": user.is_car_showroom,
    }
    response = client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 201
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert data["is_customer"] == payload["is_customer"]
    assert data["is_provider"] == payload["is_provider"]
    assert data["is_car_showroom"] == payload["is_car_showroom"]


@pytest.mark.django_db
def test_create_user_provider(client, build_user_provider):
    user = build_user_provider()
    payload = {
        "username": user.username,
        "password": "1111",
        "password_confirm": "1111",
        "email": user.email,
        "is_customer": user.is_customer,
        "is_provider": user.is_provider,
        "is_car_showroom": user.is_car_showroom,
    }
    response = client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 201
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert data["is_customer"] == payload["is_customer"]
    assert data["is_provider"] == payload["is_provider"]
    assert data["is_car_showroom"] == payload["is_car_showroom"]
