import json

import pytest

ENDPOINT = "/api/v1_provider/provider/"


@pytest.mark.django_db
def test_provider_get_endpoint(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_provider(api_client, build_provider, create_user_provider):
    api_client.force_authenticate(user=create_user_provider())
    provider = build_provider()
    payload = {
        "name": provider.name,
        "year": provider.year,
        "country": provider.country.code,
        "characteristic": provider.characteristic,
        "user": provider.user.id,
        "is_active": provider.is_active,
    }
    response = api_client.post(ENDPOINT, data=payload, content_type="application/json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_provider(api_client, create_provider):
    provider = create_provider()
    url = f"{ENDPOINT}{provider.user.id}/"
    payload = {
        "name": provider.name,
        "year": provider.year,
        "country": provider.country.code,
        "characteristic": provider.characteristic,
        "user": provider.user.id,
        "is_active": provider.is_active,
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
def test_update_provider(api_client, build_provider, create_provider):
    build_provider = build_provider()
    create_provider = create_provider()
    payload = {
        "name": build_provider.name,
        "year": build_provider.year,
        "country": build_provider.country.code,
        "characteristic": build_provider.characteristic,
        "user": create_provider.user.id,
        "is_active": build_provider.is_active,
    }
    url = f"{ENDPOINT}{create_provider.user.id}/"
    response = api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["characteristic"] == data["characteristic"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db
def test_delete_provider(api_client, create_provider):
    provider = create_provider()
    url = f"{ENDPOINT}{provider.user.id}/"
    response = api_client.delete(url)
    assert response.status_code == 405
