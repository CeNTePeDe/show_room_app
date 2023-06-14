import json

import pytest
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from user.models import User

ENDPOINT = "/api/v1_user/register/"


@pytest.mark.django_db
def test_user_endpoint(client):
    url = reverse("user-list")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user_customer(simple_api_client, build_user_customer):
    url = reverse("register")
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

    response = simple_api_client.post(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == status.HTTP_201_CREATED
    assert data["email"] == payload["email"]
    assert not User.objects.get().is_active
    assert len(mail.outbox) == 1
    assert "Activate Your Account" in mail.outbox[0].subject
    assert "Please click on the link" in mail.outbox[0].body


@pytest.mark.django_db
def test_confirm_user_customer(simple_api_client, create_user_customer):
    user = create_user_customer()
    token = default_token_generator.make_token(user)
    pk = urlsafe_base64_encode(force_bytes(user.id))
    url = reverse("activate", args=[pk, token])
    response = simple_api_client.get(url)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.get().is_active


@pytest.mark.django_db
def test_create_user_car_showroom(simple_api_client, build_user_car_showroom):
    url = reverse("register")
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

    response = simple_api_client.post(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == status.HTTP_201_CREATED
    assert data["email"] == payload["email"]
    assert not User.objects.get().is_active
    assert len(mail.outbox) == 1
    assert "Activate Your Account" in mail.outbox[0].subject
    assert "Please click on the link" in mail.outbox[0].body


@pytest.mark.django_db
def test_confirm_user_car_showroom(simple_api_client, create_user_car_showroom):
    user = create_user_car_showroom()
    token = default_token_generator.make_token(user)
    pk = urlsafe_base64_encode(force_bytes(user.id))
    url = reverse("activate", args=[pk, token])
    response = simple_api_client.get(url)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.get().is_active


@pytest.mark.django_db
def test_create_user_provider(simple_api_client, build_user_provider):
    url = reverse("register")
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

    response = simple_api_client.post(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == status.HTTP_201_CREATED
    assert data["email"] == payload["email"]
    assert not User.objects.get().is_active
    assert len(mail.outbox) == 1
    assert "Activate Your Account" in mail.outbox[0].subject
    assert "Please click on the link" in mail.outbox[0].body


@pytest.mark.django_db
def test_confirm_user_provider(simple_api_client, create_user_provider):
    user = create_user_provider()
    token = default_token_generator.make_token(user)
    pk = urlsafe_base64_encode(force_bytes(user.id))
    url = reverse("activate", args=[pk, token])
    response = simple_api_client.get(url)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.get().is_active
