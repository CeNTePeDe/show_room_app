import pytest
import json

from discount.models import CarShowRoomDiscount
from discount.serializer import CarShowRoomDiscountSerializer
from discount.tests.factories import CarShowRoomDiscountFactory

ENDPOINT = "/api/v1_discount/car_showroom_discount/"
pytestmark = pytest.mark.django_db


def test_car_showroom_discount_list(client):
    response = client.get(ENDPOINT)
    car_showroom_discount = CarShowRoomDiscount.objects.all()
    expected_data = CarShowRoomDiscountSerializer(car_showroom_discount, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


def test_create_car_showroom_discount(client):
    car_showroom_discount = CarShowRoomDiscountFactory.build()
    expected_json = {
        "discount_name": car_showroom_discount.discount_name,
        "discount_rate": car_showroom_discount.discount_rate,
    }
    response = client.post(ENDPOINT, data=expected_json)
    assert response.status_code == 201
    assert (
        json.loads(response.content)["discount_name"]
        == car_showroom_discount.discount_name
    )
    assert (
        json.loads(response.content)["discount_rate"]
        == car_showroom_discount.discount_rate
    )


def test_retrieve_car_showroom_discount(client):
    car_showroom_discount = CarShowRoomDiscountFactory.create()
    url = f"{ENDPOINT}{car_showroom_discount.id}/"
    expected_json = {
        "id": car_showroom_discount.id,
        "discount_name": car_showroom_discount.discount_name,
        "discount_rate": car_showroom_discount.discount_rate,
    }
    response = client.get(url)
    assert response.status_code == 200
    assert json.loads(response.content) == expected_json


def test_update_car_showroom_discount(client):
    old_car_showroom_discount = CarShowRoomDiscountFactory.create()
    new_car_showroom_discount = CarShowRoomDiscountFactory.build()
    new_car_showroom_discount = {
        "discount_name": new_car_showroom_discount.discount_name,
        "discount_rate": new_car_showroom_discount.discount_rate,
    }

    url = f"{ENDPOINT}{old_car_showroom_discount.id}/"
    response = client.put(
        url,
        new_car_showroom_discount,
    )
    print(new_car_showroom_discount)
    assert response.status_code == 200
    assert json.loads(response.content) == new_car_showroom_discount


def test_delete_car_showroom_discount(client):
    car_showroom_discount = CarShowRoomDiscountFactory.create()
    url = f"{ENDPOINT}{car_showroom_discount.id}/"

    response = client.delete(url)

    assert response.status_code == 204
    assert CarShowRoomDiscount.objects.all().count() == 0
