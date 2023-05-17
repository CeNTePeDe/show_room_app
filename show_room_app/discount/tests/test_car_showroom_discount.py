import pytest
import json
from discount.models import CarShowRoomDiscount
from discount.serializer import CarShowRoomDiscountSerializer

ENDPOINT = "/api/v1_discount/car_showroom_discount/"


@pytest.mark.django_db
def test_car_showroom_discount_endpoint(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_car_showroom_discount(api_client, build_car_showroom_discount):
    car_showroom = build_car_showroom_discount()
    expected_json = {
        "discount_name": car_showroom.discount_name,
        "discount_rate": car_showroom.discount_rate,
    }
    response = api_client.post(ENDPOINT, data=expected_json)
    data = response.data
    assert response.status_code == 201
    assert data["discount_name"] == expected_json["discount_name"]
    assert data["discount_rate"] == expected_json["discount_rate"]


@pytest.mark.django_db
def test_retrieve_car_showroom_discount(api_client, create_car_showroom_discount):
    car_showroom_discount = create_car_showroom_discount()
    url = f"{ENDPOINT}{car_showroom_discount.id}/"
    expected_json = {
        "id": car_showroom_discount.id,
        "discount_name": car_showroom_discount.discount_name,
        "discount_rate": car_showroom_discount.discount_rate,
    }
    response = api_client.get(url)
    data = response.data
    assert response.status_code == 200
    assert data == expected_json


@pytest.mark.django_db
def test_update_car_showroom_discount(
    api_client, create_car_showroom_discount, build_car_showroom_discount
):
    create_car_showroom_discount = create_car_showroom_discount()
    build_car_showroom_discount = build_car_showroom_discount()
    payload = {
        "discount_name": build_car_showroom_discount.discount_name,
        "discount_rate": build_car_showroom_discount.discount_rate,
    }
    url = f"{ENDPOINT}{create_car_showroom_discount.id}/"
    response = api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]


@pytest.mark.django_db
def test_delete_provider_discount(api_client, create_car_showroom_discount):
    car_showroom_discount = create_car_showroom_discount()
    url = f"{ENDPOINT}{car_showroom_discount.id}/"
    response = api_client.delete(url)

    assert response.status_code == 204
    assert CarShowRoomDiscount.objects.all().count() == 0
