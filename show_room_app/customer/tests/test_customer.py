import pytest
import json

from user.tests.factories import UserFactory

ENDPOINT = "/api/v1_customer/customer/"


@pytest.mark.django_db
def test_customer_get_endpoint(api_client):
    response = api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_customer(api_client, build_customer):
    user = UserFactory.build(username="test", is_customer=True)
    customer = build_customer()
    payload = {
        "username": customer.username,
        "balance": str(customer.balance.amount),
        "max_price": str(customer.max_price.amount),
        "user": {
            "username": user.username,
            "is_customer": user.is_customer,
        },
        "is_active": True,
    }

    response = api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 201


#
@pytest.mark.django_db
def test_retrieve_customer(api_client, create_customer):
    user = UserFactory.create(username="test_user", is_customer=True)
    customer = create_customer(user=user)
    url = f"{ENDPOINT}{customer.user.id}/"
    payload = {
        "username": customer.username,
        "balance": str(customer.balance.amount),
        "max_price": str(customer.max_price.amount),
        "is_active": customer.is_active,
        "user": {
            "username": user.username,
            "is_customer": user.is_customer,
        },
    }
    response = api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["username"] == data["username"]
    assert payload["balance"] == data["balance"]
    assert payload["max_price"] == data["max_price"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"]["username"] == data["user"]["username"]


@pytest.mark.django_db()
def test_update_customer(api_client, create_customer, build_customer):
    user = UserFactory(username="test_user", is_customer=True)
    create_customer = create_customer(user=user)
    build_customer = build_customer()
    payload = {
        "username": build_customer.username,
        "balance": str(build_customer.balance.amount),
        "max_price": str(build_customer.max_price.amount),
        "is_active": build_customer.is_active,
    }
    url = f"{ENDPOINT}{create_customer.user.id}/"
    response = api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )

    data = response.data

    assert response.status_code == 200
    assert payload["username"] == data["username"]
    assert payload["balance"] == data["balance"]
    assert payload["max_price"] == data["max_price"]
    assert payload["is_active"] == data["is_active"]


@pytest.mark.django_db
def test_delete_customer(api_client, create_customer):
    user = UserFactory(username="test_customer", is_customer=True)
    customer = create_customer(user=user)
    url = f"{ENDPOINT}{customer.user.id}/"
    response = api_client.delete(url)

    assert response.status_code == 405
