import pytest
import json

from car_showroom.tests.factories import CarShowRoomFactory, SellModelFactory
from cars.tests.factories import CarFactory
from discount.tests.factories import ProviderDiscountFactory, SeasonDiscountFactory
from provider.tests.factories import ProviderFactory
from user.tests.factories import UserFactory

ENDPOINT = "/api/v1_car_showroom/sell_car/"


@pytest.mark.django_db
def test_sell_model_get_endpoint(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_sell_model(api_client, build_sell_model):
    sell_model = build_sell_model()

    payload = {
        "car": {
            "name": sell_model.car.name,
            "model": sell_model.car.model_car,
        },
        "car_showroom": {
            "name": sell_model.car_showroom.name,
            "year": sell_model.car_showroom.year,
            "balance": str(sell_model.car_showroom.balance.amount),
            "country": sell_model.car_showroom.country.code,
            "characteristic": sell_model.car_showroom.characteristic,
            "user": {
                "username": "dada",
                "is_car_showroom": True,
            },
            "is_active": sell_model.car_showroom.is_active,
        },
        "provider": {
            {
                "name": sell_model.provider.name,
                "year": sell_model.provider.year,
                "country": sell_model.provider.country.code,
                "characteristic": sell_model.provider.characteristic,
                "user": {
                    "username": sell_model.provider.user.username,
                    "is_provider": True,
                },
                "is_active": True,
            }
        },
        "discount": {
            "discount_name": sell_model.discount.discount_name,
            "discount_rate": sell_model.discount.discount_rate,
        },
        "season_discount": {
            "discount_name": sell_model.season_discount.discount_name,
            "discount_rate": sell_model.season_discount.discount_rate,
        },
        "margin": sell_model.margin,
        "number_of_cars": sell_model.number_of_cars,
    }
    response = api_client.post(
        ENDPOINT, data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 201


# @pytest.mark.django_db
# def test_retrieve_sell_model(api_client, create_sell_model):
#     sell_model = SellModelFactory(
#             car=CarFactory(),
#             car_showroom=CarShowRoomFactory(user=UserFactory(is_car_showroom=True)),
#             provider=ProviderFactory(user=UserFactory(is_provider=True)),
#             discount=ProviderDiscountFactory(),
#             season_discount=SeasonDiscountFactory())
#     url = f"{ENDPOINT}{sell_model.id}/"
#     payload = {
#
#         "car_showroom": {
#             "name": sell_model.car_showroom.name,
#             "year": sell_model.car_showroom.year,
#             "balance": str(sell_model.car_showroom.balance.amount),
#             "country": sell_model.car_showroom.country.code,
#             "characteristic": sell_model.car_showroom.characteristic,
#             "user": {
#                 "username": sell_model.car_showroom.user.username,
#                 "is_car_showroom": sell_model.car_showroom.user.is_car_showroom,
#             },
#         },
#         "car": {
#             "name": sell_model.car.name,
#             "model": sell_model.car.model_car,
#         },
#         "provider": {
#             {
#                 "name": sell_model.provider.name,
#                 "year": sell_model.provider.year,
#                 "country": sell_model.provider.country.code,
#                 "characteristic": sell_model.provider.characteristic,
#                  "user": {
#                      "username": sell_model.provider.user.username,
#                      "is_provider": sell_model.provider.user.is_provider,
#                  },
#                 "is_active": True,
#             }
#         },
#         "discount": {
#             "discount_name": sell_model.discount.discount_name,
#             "discount_rate": sell_model.discount.discount_rate,
#         },
#         "season_discount": {
#             "discount_name": sell_model.season_discount.discount_name,
#             "discount_rate": sell_model.season_discount.discount_rate
#         },
#         "margin": sell_model.margin,
#         "number_of_cars": sell_model.number_of_cars,
#     }
#
#     response = api_client.get(url)
#     data = response.data
#
#     assert response.status_code == 200
#     # assert payload["car"] == data["car"]
#     # assert payload["car_showroom"] == data["car_showroom"]
#     # assert payload["provider"] == data["provider"]
#     # assert payload["discount"] == data["discount"]
#     # assert payload["season_discount"] == data["season_discount"]
#     assert payload["margin"] == data["margin"]
#     assert payload["number_of_cars"] == data["number_of_cars"]
#
#
# @pytest.mark.django_db
# def test_update_sell_model(api_client, create_sell_model, build_sell_model):
#     create_sell_model = create_sell_model()
#     build_sell_model = build_sell_model()
#     url = f"{ENDPOINT}{create_sell_model.id}/"
#     payload = {
#         "car": build_sell_model.car.id,
#         "car_showroom": build_sell_model.car_showroom.user.id,
#         "provider": build_sell_model.provider.user.id,
#         "discount": build_sell_model.discount.id,
#         "season_discount": build_sell_model.season_discount.id,
#         "margin": build_sell_model.margin,
#         "number_of_cars": build_sell_model.number_of_cars,
#     }
#     response = api_client.put(
#         url, data=json.dumps(payload), content_type="application/json"
#     )
#     data = response.data
#
#     assert response.status_code == 200
#     assert payload["car"] == data["car"]
#     assert payload["car_showroom"] == data["car_showroom"]
#     assert payload["provider"] == data["provider"]
#     assert payload["discount"] == data["discount"]
#     assert payload["season_discount"] == data["season_discount"]
#     assert payload["margin"] == data["margin"]
#     assert payload["number_of_cars"] == data["number_of_cars"]
#
#
# @pytest.mark.django_db
# def test_delete_sell_model(api_client, create_sell_model):
#     sell_model = create_sell_model()
#     url = f"{ENDPOINT}{sell_model.id}/"
#     response = api_client.delete(url)
#
#     assert response.status_code == 204
