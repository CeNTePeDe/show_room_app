import pytest
import json

ENDPOINT = "/api/v1_customer/customer/"


@pytest.mark.django_db
def test_customer_get_endpoint(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_customer(api_client, build_customer):
    customer = build_customer()
    payload = {
        "username": customer.username,
        "balance": str(customer.balance.amount),
        "purchases": customer.purchases.id,
        "max_price": str(customer.max_price.amount),
        "is_active": customer.is_active,
        "user": customer.user.id,
    }

    response = api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_customer(api_client, create_customer):
    customer = create_customer()
    url = f"{ENDPOINT}{customer.user.id}/"
    payload = {
        "username": customer.username,
        "balance": str(customer.balance.amount),
        "purchases": customer.purchases.id,
        "max_price": str(customer.max_price.amount),
        "is_active": customer.is_active,
        "user": customer.user.id,
    }
    response = api_client.get(url)
    data = response.data
    assert payload["username"] == data["username"]
    assert payload["balance"] == data["balance"]
    assert payload["purchases"] == data["purchases"]
    assert payload["max_price"] == data["max_price"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db()
def test_update_customer(api_client, create_customer, build_customer):
    create_customer = create_customer()
    build_customer = build_customer()
    payload = {
        "username": build_customer.username,
        "balance": str(build_customer.balance.amount),
        "purchases": create_customer.purchases.id,
        "max_price": str(build_customer.max_price.amount),
        "is_active": build_customer.is_active,
        "user": create_customer.user.id,
    }
    url = f"{ENDPOINT}{create_customer.user.id}/"
    response = api_client.get(url)
    data = response.data
    assert payload["username"] == data["username"]
    assert payload["balance"] == data["balance"]
    assert payload["purchases"] == data["purchases"]
    assert payload["max_price"] == data["max_price"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db
def test_delete_customer(api_client, create_customer):
    customer = create_customer()
    url = f"{ENDPOINT}{customer.user.id}/"
    respose = api_client.delete(url)
    assert respose.status_code == 405
