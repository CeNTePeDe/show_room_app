import pytest
import json

from rest_framework_simplejwt.tokens import AccessToken

ENDPOINT = "/api/v1_customer/customer/"


@pytest.mark.django_db
def test_customer_get_endpoint(simple_api_client):
    response = simple_api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_customer(simple_api_client, build_customer, create_user_customer):
    user = create_user_customer()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    customer = build_customer(user=user)
    payload = {
        "username": customer.username,
        "balance": str(customer.balance.amount),
        "model_car": customer.model_car,
        "user": customer.user.id,
        "is_active": True,
    }

    response = simple_api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 201


#
@pytest.mark.django_db
def test_retrieve_customer(simple_api_client, create_customer, create_user_customer):
    user = create_user_customer()
    customer = create_customer(user=user)
    url = f"{ENDPOINT}{customer.user.id}/"
    payload = {
        "username": customer.username,
        "balance": str(customer.balance.amount),
        "model_car": customer.model_car,
        "is_active": customer.is_active,
        "user": customer.user.id,
    }
    response = simple_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["username"] == data["username"]
    assert payload["balance"] == data["balance"]
    assert payload["model_car"] == data["model_car"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db()
def test_update_customer(
    simple_api_client, create_customer, build_customer, create_user_customer
):
    user = create_user_customer()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    create_customer = create_customer(user=user)
    customer = build_customer()
    payload = {
        "username": customer.username,
        "balance": str(customer.balance.amount),
        "model_car": customer.model_car,
        "is_active": customer.is_active,
        "user": user.id,
    }
    url = f"{ENDPOINT}{create_customer.user.id}/"
    response = simple_api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )

    data = response.data

    assert response.status_code == 200
    assert payload["username"] == data["username"]
    assert payload["balance"] == data["balance"]
    assert payload["is_active"] == data["is_active"]


@pytest.mark.django_db
def test_delete_customer(simple_api_client, create_customer, create_user_customer):
    user = create_user_customer()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    customer = create_customer(user=user)
    url = f"{ENDPOINT}{customer.user.id}/"
    response = simple_api_client.delete(url)

    assert response.status_code == 405
