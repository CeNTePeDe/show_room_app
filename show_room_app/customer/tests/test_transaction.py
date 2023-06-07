import json
from datetime import date

import pytest

from car_showroom.tests.factories import CarShowRoomFactory
from cars.tests.factories import CarFactory

ENDPOINT = "/api/v1_customer/transaction/"


@pytest.mark.django_db
def test_transaction_endpoint(simple_api_client):
    response = simple_api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_transaction(
    admin_api_client, create_customer, create_user_customer, create_user_car_showroom
):
    car = CarFactory()
    user = create_user_customer()
    customer = create_customer(user=user)
    user_car_showroom = create_user_car_showroom()
    car_showroom = CarShowRoomFactory(user=user_car_showroom)
    payload = {
        "car": car.name,
        "customer": customer.username,
        "car_showroom": car_showroom.name,
        "price": "10000.0",
        "date": date.today().strftime("%Y-%m-%d"),
    }
    response = admin_api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_transaction(admin_api_client, create_transaction):
    transaction = create_transaction()
    url = f"{ENDPOINT}{transaction.id}/"
    payload = {
        "car": transaction.car.name,
        "customer": transaction.customer.username,
        "car_showroom": transaction.car_showroom.name,
        "price": str(transaction.price.amount),
        "date": date.today().strftime("%Y-%m-%d"),
    }
    response = admin_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["car_showroom"] == data["car_showroom"]
    assert payload["car"] == data["car"]
    assert payload["price"] == data["price"]


@pytest.mark.django_db
def test_delete_transaction(admin_api_client, create_transaction):
    transaction = create_transaction()
    url = f"{ENDPOINT}{transaction.id}/"
    response = admin_api_client.delete(url)
    assert response.status_code == 405
