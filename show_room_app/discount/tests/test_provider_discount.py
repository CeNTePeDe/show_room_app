import pytest
import json

from rest_framework_simplejwt.tokens import AccessToken

from discount.models import ProviderDiscount
from provider.tests.factories import ProviderFactory

ENDPOINT = "/api/v1_discount/provider_discount/"


@pytest.mark.django_db
def test_provider_discount_endpoint(simple_api_client):
    response = simple_api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_provider_discount(
    simple_api_client, build_provider_discount, create_user_provider
):
    user = create_user_provider()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    provider = ProviderFactory(user=user)
    provider_discount = build_provider_discount(provider_discount=provider)

    payload = {
        "discount_name": provider_discount.discount_name,
        "discount_rate": provider_discount.discount_rate,
        "date_start": provider_discount.date_start,
        "date_finish": provider_discount.date_finish,
        "special_discount": True,
        "is_active": True,
        "provider_discount": provider_discount.provider_discount.user.id,
    }
    response = simple_api_client.post(ENDPOINT, data=payload)
    data = response.data

    assert response.status_code == 201
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]


@pytest.mark.django_db
def test_retrieve_provider_discount(
    simple_api_client, create_provider_discount, create_user_provider
):
    user = create_user_provider()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    provider = ProviderFactory(user=user)

    provider_discount = create_provider_discount(provider_discount=provider)
    url = f"{ENDPOINT}{provider_discount.id}/"
    payload = {
        "discount_name": provider_discount.discount_name,
        "discount_rate": provider_discount.discount_rate,
        "date_start": provider_discount.date_start.strftime("%Y-%m-%d"),
        "date_finish": provider_discount.date_finish.strftime("%Y-%m-%d"),
        "special_discount": True,
        "is_active": True,
        "provider_discount": provider_discount.provider_discount.user.id,
    }
    response = simple_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]
    assert data["date_start"] == payload["date_start"]
    assert data["date_finish"] == payload["date_finish"]
    assert data["provider_discount"] == payload["provider_discount"]


@pytest.mark.django_db
def test_update_provider_discount(
    simple_api_client,
    create_provider_discount,
    build_provider_discount,
    create_user_provider,
):
    user = create_user_provider()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    provider = ProviderFactory(user=user)
    create_provider_discount = create_provider_discount(provider_discount=provider)
    build_provider_discount = build_provider_discount(provider_discount=provider)
    payload = {
        "discount_name": build_provider_discount.discount_name,
        "discount_rate": build_provider_discount.discount_rate,
        "date_start": build_provider_discount.date_start.strftime("%Y-%m-%d"),
        "date_finish": build_provider_discount.date_finish.strftime("%Y-%m-%d"),
        "special_discount": True,
        "is_active": True,
        "provider_discount": create_provider_discount.provider_discount.user.id,
    }
    url = f"{ENDPOINT}{create_provider_discount.id}/"
    response = simple_api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 200
    assert data["discount_name"] == payload["discount_name"]
    assert data["discount_rate"] == payload["discount_rate"]
    assert data["date_start"] == payload["date_start"]
    assert data["date_finish"] == payload["date_finish"]
    assert data["provider_discount"] == payload["provider_discount"]


@pytest.mark.django_db
def test_delete_provider_discount(
    simple_api_client, create_provider_discount, create_user_provider
):
    user = create_user_provider()
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    provider = ProviderFactory(user=user)
    provider_discount = create_provider_discount(provider_discount=provider)
    url = f"{ENDPOINT}{provider_discount.id}/"
    response = simple_api_client.delete(url)

    assert response.status_code == 405
    assert ProviderDiscount.objects.all().count() == 1
