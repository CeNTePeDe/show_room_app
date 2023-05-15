import pytest
import json

from discount.models import ProviderDiscount
from discount.serializer import ProviderDiscountSerializer

ENDPOINT = "/api/v1_discount/provider_discount/"


@pytest.mark.django_db
def test_provider_discount_list(client):
    response = client.get(ENDPOINT)
    provider_discount = ProviderDiscount.objects.all()
    expected_data = ProviderDiscountSerializer(provider_discount, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_provider_discount(client, build_provider_discount):
    expected_json = {
        "discount_name": build_provider_discount.discount_name,
        "discount_rate": build_provider_discount.discount_rate,
    }
    response = client.post(ENDPOINT, data=expected_json)
    data = response.data
    assert response.status_code == 201
    assert data["discount_name"] == expected_json["discount_name"]
    assert data["discount_rate"] == expected_json["discount_rate"]


@pytest.mark.django_db
def test_retrieve_provider_discount(client, create_provider_discount):
    url = f"{ENDPOINT}{create_provider_discount.id}/"
    expected_json = {
        "id": create_provider_discount.id,
        "discount_name": create_provider_discount.discount_name,
        "discount_rate": create_provider_discount.discount_rate,
    }
    response = client.get(url)
    data = response.data
    assert response.status_code == 200
    assert data == expected_json


@pytest.mark.django_db
def test_update_provider_discount(
    client, create_provider_discount, build_provider_discount
):
    payload = {
        "discount_name": build_provider_discount.discount_name,
        "discount_rate": build_provider_discount.discount_rate,
    }
    url = f"{ENDPOINT}{create_provider_discount.id}/"
    response = client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]


@pytest.mark.django_db
def test_delete_provider_discount(client, create_provider_discount):
    url = f"{ENDPOINT}{create_provider_discount.id}/"
    response = client.delete(url)

    assert response.status_code == 204
    assert ProviderDiscount.objects.all().count() == 0
