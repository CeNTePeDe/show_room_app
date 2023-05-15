import pytest
import json

ENDPOINT = "/api/v1_customer/customer/"


@pytest.mark.django_db
def test_customer_get_endpoint(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_customer(client, build_customer):
    payload = {
        "username": build_customer.username,
        "balance": build_customer.balance.amount,
        "purchases": build_customer.purchases.id,
        "max_price": build_customer.max_price.amount,
        "is_active": build_customer.is_active,
        "user": build_customer.user.id,
    }
    response = client.post(ENDPOINT, data=payload, content_type="application/json")
    assert response.status_code == 201
