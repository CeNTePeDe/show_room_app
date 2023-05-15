import pytest
import json

ENDPOINT = "/api/v1_provider/provider/"


@pytest.mark.django_db
def test_provider_get_endpoint(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_provider(client, build_provider):
    payload = {
        "name": build_provider.name,
        "year": build_provider.year,
        "country": build_provider.country.code,
        "characteristic": build_provider.characteristic,
        "user": build_provider.user.id,
        "is_active": build_provider.is_active,
    }
    response = client.post(ENDPOINT, data=payload, content_type="application/json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_provider(client, create_provider):
    url = f"{ENDPOINT}{create_provider.user.id}/"
    payload = {
        "name": create_provider.name,
        "year": create_provider.year,
        "country": create_provider.country.code,
        "characteristic": create_provider.characteristic,
        "user": create_provider.user.id,
        "is_active": create_provider.is_active,
    }
    response = client.get(url)
    data = response.data
    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["characteristic"] == data["characteristic"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"] == data["user"]


@pytest.mark.django_db
def test_delete_provider(client, create_provider):
    url = f"{ENDPOINT}{create_provider.user.id}"
    response = client.delete(url)
    assert response.status_code == 405