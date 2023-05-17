import json
import pytest

ENDPOINT = "/api/v1_customer/transaction/"


@pytest.mark.django_db
def test_transaction_endpoint(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_transaction(api_client, build_transaction):
    transaction = build_transaction()
    payload = {
        "car_showroom": transaction.car_showroom.user.id,
        "price": str(transaction.price.amount),
        "discount": transaction.discount.id,
        "season_discount": transaction.season_discount.id,
    }
    response = api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_transaction(api_client, create_transaction):
    transaction = create_transaction()
    url = f"{ENDPOINT}{transaction.id}/"
    payload = {
        "car_showroom": transaction.car_showroom.user.id,
        "price": str(transaction.price.amount),
        "discount": transaction.discount.id,
        "season_discount": transaction.season_discount.id,
    }
    response = api_client.get(url)
    data = response.data
    assert response.status_code == 200
    assert payload["car_showroom"] == data["car_showroom"]
    assert payload["price"] == data["price"]
    assert payload["discount"] == data["discount"]
    assert payload["season_discount"] == data["season_discount"]


@pytest.mark.django_db
def test_update_transaction(api_client, create_transaction, build_transaction):
    create_transaction = create_transaction()
    build_transaction = build_transaction()
    payload = {
        "car_showroom": build_transaction.car_showroom.user.id,
        "price": str(build_transaction.price.amount),
        "discount": build_transaction.discount.id,
        "season_discount": build_transaction.season_discount.id,
    }
    url = f"{ENDPOINT}{create_transaction.id}/"

    response = api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert payload["car_showroom"] == data["car_showroom"]
    assert payload["price"] == data["price"]
    assert payload["discount"] == data["discount"]
    assert payload["season_discount"] == data["season_discount"]


@pytest.mark.django_db
def test_delete_transaction(api_client, create_transaction):
    transaction = create_transaction()
    url = f"{ENDPOINT}{transaction.id}/"
    response = api_client.delete(url)
    assert response.status_code == 405
