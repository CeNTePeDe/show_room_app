import json
import pytest

ENDPOINT = "/api/v1_customer/transaction/"


@pytest.mark.django_db
def test_transaction_endpoint(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_transaction(client, build_transaction):
    payload = {
        "car_showroom": build_transaction.car_showroom.user.id,
        "price": str(build_transaction.price.amount),
        "discount": build_transaction.discount.id,
        "season_discount": build_transaction.season_discount.id,
    }
    response = client.post(ENDPOINT, data=payload, content_type="application/json")
    assert response.status_code == 201
