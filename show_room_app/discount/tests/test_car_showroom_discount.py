import pytest
import json
from discount.models import CarShowRoomDiscount
from discount.serializer import CarShowRoomDiscountSerializer

ENDPOINT = "/api/v1_discount/car_showroom_discount/"


@pytest.mark.django_db
def test_car_showroom_list(client):
    response = client.get(ENDPOINT)
    car_showroom_discount = CarShowRoomDiscount.objects.all()
    expected_data = CarShowRoomDiscountSerializer(car_showroom_discount, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_car_showroom(client, build_car_showroom):
    expected_json = {
        "discount_name": build_car_showroom.discount_name,
        "discount_rate": build_car_showroom.discount_rate,
    }
    response = client.post(ENDPOINT, data=expected_json)
    data = response.data
    assert response.status_code == 201
    assert data["discount_name"] == expected_json["discount_name"]
    assert data["discount_rate"] == expected_json["discount_rate"]


@pytest.mark.django_db
def test_retrieve_car_showroom_discount(client, create_car_showroom_discount):
    url = f"{ENDPOINT}{create_car_showroom_discount.id}/"
    expected_json = {
        "id": create_car_showroom_discount.id,
        "discount_name": create_car_showroom_discount.discount_name,
        "discount_rate": create_car_showroom_discount.discount_rate,
    }
    response = client.get(url)
    data = response.data
    assert response.status_code == 200
    assert data == expected_json


@pytest.mark.django_db
def test_update_car_showroom_discount(
    client, create_car_showroom_discount, build_car_showroom_discount
):
    payload = {
        "discount_name": build_car_showroom_discount.discount_name,
        "discount_rate": build_car_showroom_discount.discount_rate,
    }
    url = f"{ENDPOINT}{create_car_showroom_discount.id}/"
    response = client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]


@pytest.mark.django_db
def test_delete_provider_discount(client, create_car_showroom_discount):
    url = f"{ENDPOINT}{create_car_showroom_discount.id}/"
    response = client.delete(url)

    assert response.status_code == 204
    assert CarShowRoomDiscount.objects.all().count() == 0
