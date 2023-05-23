import json

import pytest

from user.tests.factories import UserFactory

ENDPOINT = "/api/v1_provider/provider/"


@pytest.mark.django_db
def test_provider_get_endpoint(api_client):
    response = api_client.get(ENDPOINT)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_provider(api_client, build_provider):
    provider = build_provider()
    user = UserFactory.build(username="mytestuser", is_provider=True)
    payload = {
        "name": provider.name,
        "year": int(provider.year),
        "country": provider.country.code,
        "characteristic": provider.characteristic,
        "user": {
            "username": user.username,
            "is_provider": user.is_provider,
        },
        "is_active": True,
    }
    response = api_client.post(
        ENDPOINT,
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_provider(api_client, create_provider):
    user = UserFactory.create(username="test_user", is_provider=True)
    provider = create_provider(user=user)
    url = f"{ENDPOINT}{provider.user.id}/"
    payload = {
        "name": provider.name,
        "year": int(provider.year),
        "country": provider.country,
        "characteristic": provider.characteristic,
        "user": {
            "username": user.username,
            "is_provider": user.is_provider,
        },
        "is_active": provider.is_active,
    }
    response = api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["characteristic"] == data["characteristic"]
    assert payload["is_active"] == data["is_active"]
    assert payload["user"]["username"] == data["user"]["username"]
    assert payload["user"]["is_provider"] == data["user"]["is_provider"]


@pytest.mark.django_db
def test_update_provider(api_client, build_provider, create_provider):
    user = UserFactory(username="www", is_provider=True)
    build_provider = build_provider()
    provider = create_provider(user=user)
    payload = {
        "name": build_provider.name,
        "year": int(build_provider.year),
        "country": build_provider.country.code,
        "characteristic": build_provider.characteristic,
        "is_active": build_provider.is_active,
    }
    url = f"{ENDPOINT}{provider.user.id}/"
    response = api_client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data

    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["characteristic"] == data["characteristic"]
    assert payload["is_active"] == data["is_active"]


@pytest.mark.django_db
def test_delete_provider(api_client, create_provider):
    user = UserFactory(username="my_test", is_provider=True)
    provider = create_provider(user=user)
    url = f"{ENDPOINT}{provider.user.id}/"
    response = api_client.delete(url)
    assert response.status_code == 405
