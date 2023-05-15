import pytest
import json

ENDPOINT = "/api/v1_car_showroom/sell_car/"


@pytest.mark.django_db
def test_sell_model_get_endpoint(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_sell_model(client, build_sell_model):
    payload = {
        "car": build_sell_model.car.id,
        "car_showroom": build_sell_model.car_showroom.user.id,
        "provider": build_sell_model.provider.user.id,
        "discount": build_sell_model.discount.id,
        "season_discount": build_sell_model.season_discount.id,
        "margin": build_sell_model.margin,
        "number_of_cars": build_sell_model.number_of_cars,
    }
    response = client.post(ENDPOINT, data=payload, content_type="application/json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_sell_model(client, create_sell_model):
    url = f"{ENDPOINT}{create_sell_model.id}/"
    payload = {
        "car": create_sell_model.car.id,
        "car_showroom": create_sell_model.car_showroom.user.id,
        "provider": create_sell_model.provider.user.id,
        "discount": create_sell_model.discount.id,
        "season_discount": create_sell_model.season_discount.id,
        "margin": create_sell_model.margin,
        "number_of_cars": create_sell_model.number_of_cars,
    }
    response = client.get(url)
    data = response.data
    assert response.status_code == 200
    assert payload["car"] == data["car"]
    assert payload["car_showroom"] == data["car_showroom"]
    assert payload["provider"] == data["provider"]
    assert payload["discount"] == data["discount"]
    assert payload["season_discount"] == data["season_discount"]
    assert payload["margin"] == data["margin"]
    assert payload["number_of_cars"] == data["number_of_cars"]


@pytest.mark.django_db
def test_update_sell_model(client, create_sell_model, build_sell_model):
    url = f"{ENDPOINT}{create_sell_model.id}/"
    payload = {
        "car": build_sell_model.car.id,
        "car_showroom": build_sell_model.car_showroom.user.id,
        "provider": build_sell_model.provider.user.id,
        "discount": build_sell_model.discount.id,
        "season_discount": build_sell_model.season_discount.id,
        "margin": build_sell_model.margin,
        "number_of_cars": build_sell_model.number_of_cars,
    }
    response = client.put(
        url, data=json.dumps(payload), content_type="application/json"
    )
    data = response.data
    assert response.status_code == 200
    assert payload["car"] == data["car"]
    assert payload["car_showroom"] == data["car_showroom"]
    assert payload["provider"] == data["provider"]
    assert payload["discount"] == data["discount"]
    assert payload["season_discount"] == data["season_discount"]
    assert payload["margin"] == data["margin"]
    assert payload["number_of_cars"] == data["number_of_cars"]


@pytest.mark.django_db
def test_delete_sell_model(client, create_sell_model):
    url = f"{ENDPOINT}{create_sell_model.id}/"
    response = client.delete(url)
    assert response.status_code == 204
