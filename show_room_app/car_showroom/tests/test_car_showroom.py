import json
import pytest

ENDPOINT = "/api/v1_car_showroom/car_showroom/"


@pytest.mark.django_db
def test_car_showroom_get_endpoint(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car_showroom(api_client, build_car_showroom):
    car_showroom = build_car_showroom()
    payload = {
        "name": car_showroom.name,
        "year": car_showroom.year,
        "balance": str(car_showroom.balance.amount),
        "country": car_showroom.country.code,
        "characteristic": car_showroom.characteristic,
        "user": car_showroom.user.id,
        "is_active": car_showroom.is_active,
    }
    print(payload)
    response = api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_car_showroom(api_client, create_car_showroom):
    car_showroom = create_car_showroom()
    url = f"{ENDPOINT}{car_showroom.user.id}/"
    payload = {
        "name": car_showroom.name,
        "year": car_showroom.year,
        "balance": car_showroom.balance.amount,
        "country": car_showroom.country.code,
        "characteristic": car_showroom.characteristic,
        "is_active": car_showroom.is_active,
        "user": car_showroom.user.id,
    }
    response = api_client.get(url)
    data = response.data
    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["characteristic"] == data["characteristic"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db
def test_update_car_showroom(api_client, create_car_showroom, build_car_showroom):
    create_car_showroom = create_car_showroom()
    build_car_showroom = build_car_showroom()
    payload = {
        "name": build_car_showroom.name,
        "year": build_car_showroom.year,
        "country": build_car_showroom.country.name,
        "characteristic": build_car_showroom.characteristic,
        "balance": str(build_car_showroom.balance.amount),
        "is_active": build_car_showroom.is_active,
        "user": create_car_showroom.user.id,
    }
    url = f"{ENDPOINT}{create_car_showroom.user.id}/"
    print(payload)
    response = api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_car_showroom(api_client, create_car_showroom):
    car_showroom = create_car_showroom()
    url = f"{ENDPOINT}{car_showroom.user.id}/"
    response = api_client.delete(url)
    assert response.status_code == 405
