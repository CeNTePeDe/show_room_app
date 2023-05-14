import pytest
import json

from discount.models import ProviderDiscount
from discount.serializer import ProviderDiscountSerializer
from discount.tests.factories import ProviderDiscountFactory

ENDPOINT = "/api/v1_discount/provider_discount/"
pytestmark = pytest.mark.django_db


def test_provider_discount_list(client):
    response = client.get(ENDPOINT)
    provider_discount = ProviderDiscount.objects.all()
    expected_data = ProviderDiscountSerializer(provider_discount, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


def test_create_provider_discount(client):
    provider_discount = ProviderDiscountFactory.build()
    expected_json = {
        "discount_name": provider_discount.discount_name,
        "discount_rate": provider_discount.discount_rate,
    }
    response = client.post(ENDPOINT, data=expected_json)
    assert response.status_code == 201
    assert (json.loads(response.content))[
        "discount_name"
    ] == provider_discount.discount_name
    assert (json.loads(response.content))[
        "discount_rate"
    ] == provider_discount.discount_rate


def test_retrieve_provider_discount(client):
    provider_discount = ProviderDiscountFactory.create()
    url = f"{ENDPOINT}{provider_discount.id}/"
    expected_json = {
        "id": provider_discount.id,
        "discount_name": provider_discount.discount_name,
        "discount_rate": provider_discount.discount_rate,
    }
    response = client.get(url)
    assert response.status_code == 200
    assert json.loads(response.content) == expected_json


def test_update_provider_discount(client):
    old_provider_discount = ProviderDiscountFactory.create()
    new_provider_discount = ProviderDiscountFactory.build()
    new_provider_discount = {
        "discount_name": new_provider_discount.discount_name,
        "discount_rate": new_provider_discount.discount_rate,
    }

    url = f"{ENDPOINT}{old_provider_discount.id}/"
    response = client.put(
        url,
        new_provider_discount,
    )
    print(new_provider_discount)
    assert response.status_code == 200
    assert json.loads(response.content) == new_provider_discount


def test_delete_provider_discount(client):
    provider_discount = ProviderDiscountFactory.create()
    url = f"{ENDPOINT}{provider_discount.id}/"

    response = client.delete(url)

    assert response.status_code == 204
    assert ProviderDiscount.objects.all().count() == 0
