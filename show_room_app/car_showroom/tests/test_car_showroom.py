import json
import pytest

ENDPOINT = "/api/v1_car_showroom/car_showroom/"


@pytest.mark.django_db
def test_car_showroom_get_endpoint(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car_showroom(client, build_car_showroom):
    payload = {
        "name": build_car_showroom.name,
        "year": build_car_showroom.year,
        "balance": str(build_car_showroom.balance.amount),
        "country": build_car_showroom.country.code,
        "characteristic": build_car_showroom.characteristic,
        "user": build_car_showroom.user.id,
        "is_active": build_car_showroom.is_active,
    }
    response = client.post(ENDPOINT, data=payload, content_type="application/json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_car_showroom(client, create_car_showroom):
    url = f"{ENDPOINT}{create_car_showroom.user.id}/"
    payload = {
        "name": create_car_showroom.name,
        "year": create_car_showroom.year,
        "balance": create_car_showroom.balance.amount,
        "country": create_car_showroom.country.code,
        "characteristic": create_car_showroom.characteristic,
        "is_active": create_car_showroom.is_active,
        "user": create_car_showroom.user.id,
    }
    response = client.get(url)
    data = response.data
    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["characteristic"] == data["characteristic"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db
def test_update_car_showroom(client, create_car_showroom, build_car_showroom):
    payload = {
        "name": build_car_showroom.name,
        "year": build_car_showroom.year,
        "country": build_car_showroom.country.name,
        "characteristic": build_car_showroom.characteristic,
        "balance": str(build_car_showroom.balance.amount),
        "user": build_car_showroom.user.id,
        "is_active": build_car_showroom.is_active,
    }
    url = f"{ENDPOINT}{create_car_showroom.user.id}/"

    response = client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_car_showroom(client,create_car_showroom):
    url = f"{ENDPOINT}{create_car_showroom.user.id}/"
    response = client.delete(url)
    assert response.status_code == 405

