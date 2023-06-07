import json

import pytest
from rest_framework_simplejwt.tokens import AccessToken

from user.models import User
from user.tests.factories import UserFactory

ENDPOINT = "/api/v1_provider/provider/"


@pytest.mark.django_db
def test_provider_get_endpoint(simple_api_client):
    response = simple_api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_provider(simple_api_client, build_provider):
    user = UserFactory.build(is_provider=True)
    access_token = AccessToken.for_user(user)
    simple_api_client.force_authenticate(user=user, token=str(access_token))
    provider = build_provider(user=user)
    payload = {
        "name": provider.name,
        "year": int(provider.year),
        "country": provider.country.code,
        "user": provider.user.id,
        "is_active": True,
    }
    print(payload)
    response = simple_api_client.post(
        ENDPOINT,
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_provider(simple_api_client, create_provider):
    user = UserFactory.create(username="test_user", is_provider=True)
    provider = create_provider(user=user)
    url = f"{ENDPOINT}{provider.user.id}/"
    payload = {
        "name": provider.name,
        "year": int(provider.year),
        "country": provider.country,
        "user": provider.user.id,
        "is_active": provider.is_active,
    }
    response = simple_api_client.get(url)
    data = response.data

    assert response.status_code == 200
    assert payload["name"] == data["name"]
    assert payload["year"] == data["year"]
    assert payload["is_active"] == data["is_active"]


# @pytest.mark.django_db
# def test_update_provider(provider_api_client, build_provider, create_provider):
#     user = UserFactory(username="www", is_provider=True)
#     build_provider = build_provider()
#     provider = create_provider(user=user)
#     payload = {
#         "name": build_provider.name,
#         "year": int(build_provider.year),
#         "country": build_provider.country.code,
#         "is_active": build_provider.is_active,
#     }
#     url = f"{ENDPOINT}{provider.user.id}/"
#     response = provider_api_client.put(
#         url, data=json.dumps(payload), content_type="application/json"
#     )
#     data = response.data
#
#     assert response.status_code == 200
#     assert payload["name"] == data["name"]
#     assert payload["year"] == data["year"]
#     assert payload["is_active"] == data["is_active"]
#


@pytest.mark.django_db
def test_delete_provider(provider_api_client, create_provider):
    user = UserFactory(username="my_test", is_provider=True)
    provider = create_provider(user=user)
    url = f"{ENDPOINT}{provider.user.id}/"
    response = provider_api_client.delete(url)
    assert response.status_code == 405
