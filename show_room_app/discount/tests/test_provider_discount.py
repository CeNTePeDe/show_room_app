import pytest
import json

from discount.models import ProviderDiscount

ENDPOINT = "http://localhost:8000/api/v1_discount/provider_discount/"


@pytest.mark.django_db
def test_provider_discount_endpoint(api_client):
    response = api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_provider_discount(api_client, build_provider_discount):
    provider_discount = build_provider_discount()
    expected_json = {
        "discount_name": provider_discount.discount_name,
        "discount_rate": provider_discount.discount_rate,
    }
    response = api_client.post(ENDPOINT, data=expected_json)
    data = response.data

    assert response.status_code == 201
    assert data["discount_name"] == expected_json["discount_name"]
    assert data["discount_rate"] == expected_json["discount_rate"]


@pytest.mark.django_db
def test_retrieve_provider_discount(api_client, create_provider_discount):
    provider_discount = create_provider_discount()
    url = f"{ENDPOINT}{provider_discount.id}/"
    expected_json = {
        "id": provider_discount.id,
        "discount_name": provider_discount.discount_name,
        "discount_rate": provider_discount.discount_rate,
    }
    response = api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert data == expected_json


@pytest.mark.django_db
def test_update_provider_discount(
    api_client, create_provider_discount, build_provider_discount
):
    create_provider_discount = create_provider_discount()
    build_provider_discount = build_provider_discount()
    payload = {
        "discount_name": build_provider_discount.discount_name,
        "discount_rate": build_provider_discount.discount_rate,
    }
    url = f"{ENDPOINT}{create_provider_discount.id}/"
    response = api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]


@pytest.mark.django_db
def test_delete_provider_discount(api_client, create_provider_discount):
    provider_discount = create_provider_discount()
    url = f"{ENDPOINT}{provider_discount.id}/"
    response = api_client.delete(url)

    assert response.status_code == 204
    assert ProviderDiscount.objects.all().count() == 0
