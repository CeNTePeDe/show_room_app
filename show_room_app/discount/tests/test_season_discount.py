import pytest
import json

from discount.models import SeasonDiscount
from discount.serializer import SeasonDiscountSerializer
from discount.tests.factories import SeasonDiscountFactory

ENDPOINT = "/api/v1_discount/season_discount/"
pytestmark = pytest.mark.django_db


def test_season_discount_list(client):
    response = client.get(ENDPOINT)
    season_discount = SeasonDiscount.objects.all()
    expected_data = SeasonDiscountSerializer(season_discount, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


def test_create_season_discount(client):
    season_discount = SeasonDiscountFactory.build()
    expected_json = {
        "discount_name": season_discount.discount_name,
        "date_start": season_discount.date_start,
        "date_finish": season_discount.date_finish,
        "discount_rate": season_discount.discount_rate,
    }
    response = client.post(ENDPOINT, data=expected_json)
    assert response.status_code == 201
    assert (
        json.loads(response.content)["discount_name"] == season_discount.discount_name
    )
    assert json.loads(response.content)["date_start"] == season_discount.date_start
    assert json.loads(response.content)["date_finish"] == season_discount.date_finish
    assert (
        json.loads(response.content)["discount_rate"] == season_discount.discount_rate
    )


def test_retrieve_season_discount(client):
    season_discount = SeasonDiscountFactory.create()
    url = f"{ENDPOINT}{season_discount.id}/"
    expected_json = {
        "id": season_discount.id,
        "discount_name": season_discount.discount_name,
        "date_start": season_discount.date_start,
        "date_finish": season_discount.date_finish,
        "discount_rate": season_discount.discount_rate,
    }
    response = client.get(url)
    assert response.status_code == 200
    assert json.loads(response.content) == expected_json


def test_update_season_discount(client):
    old_season_discount = SeasonDiscountFactory.create()
    new_season_discount = SeasonDiscountFactory.build()
    new_season_discount = {
        "discount_name": new_season_discount.discount_name,
        "date_start": new_season_discount.date_start,
        "date_finish": new_season_discount.date_finish,
        "discount_rate": new_season_discount.discount_rate,
    }
    url = f"{ENDPOINT}{old_season_discount.id}/"
    response = client.put(
        url,
        new_season_discount,
        format="json",
    )
    assert response.status_code == 200
    assert json.loads(response.content) == new_season_discount


def test_delete_provider_discount(client):
    season_discount = SeasonDiscountFactory.create()
    url = f"{ENDPOINT}{season_discount.id}/"

    response = client.delete(url)

    assert response.status_code == 204
    assert SeasonDiscount.objects.all().count() == 0
