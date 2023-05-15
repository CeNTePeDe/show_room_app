import pytest
import json

from discount.models import SeasonDiscount
from discount.serializer import SeasonDiscountSerializer
from discount.tests.factories import SeasonDiscountFactory

ENDPOINT = "/api/v1_discount/season_discount/"


@pytest.mark.django_db
def test_season_discount_list(client):
    response = client.get(ENDPOINT)
    season_discount = SeasonDiscount.objects.all()
    expected_data = SeasonDiscountSerializer(season_discount, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_season_discount(client, build_season_discount):
    expected_json = {
        "discount_name": build_season_discount.discount_name,
        "date_start": build_season_discount.date_start,
        "date_finish": build_season_discount.date_finish,
        "discount_rate": build_season_discount.discount_rate,
    }
    response = client.post(ENDPOINT, data=expected_json)
    data = response.data
    assert response.status_code == 201
    assert data["discount_name"] == expected_json["discount_name"]
    assert data["date_start"] == expected_json["date_start"]
    assert data["date_finish"] == expected_json["date_finish"]
    assert data["discount_rate"] == expected_json["discount_rate"]


@pytest.mark.django_db
def test_retrieve_season_discount(client, create_season_discount):
    url = f"{ENDPOINT}{create_season_discount.id}/"
    expected_json = {
        "id": create_season_discount.id,
        "discount_name": create_season_discount.discount_name,
        "date_start": create_season_discount.date_start,
        "date_finish": create_season_discount.date_finish,
        "discount_rate": create_season_discount.discount_rate,
    }
    response = client.get(url)
    assert response.status_code == 200
    assert json.loads(response.content) == expected_json


@pytest.mark.django_db
def test_update_season_discount(client, build_season_discount, create_season_discount):
    payload = {
        "discount_name": build_season_discount.discount_name,
        "date_start": build_season_discount.date_start,
        "date_finish": build_season_discount.date_finish,
        "discount_rate": build_season_discount.discount_rate,
    }
    url = f"{ENDPOINT}{create_season_discount.id}/"
    response = client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["date_start"] == payload["date_start"]
    assert data["date_finish"] == payload["date_finish"]
    assert data["discount_rate"] == payload["discount_rate"]


@pytest.mark.django_db
def test_delete_provider_discount(client, create_season_discount):
    url = f"{ENDPOINT}{create_season_discount.id}/"

    response = client.delete(url)

    assert response.status_code == 204
    assert SeasonDiscount.objects.all().count() == 0
