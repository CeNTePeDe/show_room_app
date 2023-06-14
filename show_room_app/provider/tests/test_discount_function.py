from datetime import date
import pytest
from unittest.mock import patch

from car_showroom.tests.factories import CarShowRoomFactory
from core.provider_discount import (
    get_season_discount_from_provider,
    get_provider_discount_for_special_client,
)


@pytest.mark.django_db
def test_get_season_discount_from_provider(
    create_season_discount, create_user_provider, create_provider
):
    user = create_user_provider()
    provider = create_provider(user=user)
    discount = create_season_discount(provider_discount=provider)
    season_discount = get_season_discount_from_provider(
        sale_date=date.today(), provider_id=provider.user.id
    )

    assert season_discount == discount.discount_rate


@pytest.mark.django_db
def test_get_season_discount_from_provider_no_discount(
    create_provider, create_user_provider
):
    user = create_user_provider()
    provider = create_provider(user=user)
    provider_id = provider.user.id
    season_discount = get_season_discount_from_provider(
        sale_date=date.today(), provider_id=provider_id
    )

    assert season_discount == 0


@pytest.mark.django_db
def test_provider_discount_for_first_purchase(
    create_provider,
    create_user_car_showroom,
    create_user_provider,
    create_first_purchase_discount,
):
    user_provider = create_user_provider()
    user_car_showroom = create_user_car_showroom()
    provider = create_provider(user=user_provider)
    car_showroom = CarShowRoomFactory(user=user_car_showroom)
    discount = create_first_purchase_discount(provider_discount=provider)
    first_purchase_discount = get_provider_discount_for_special_client(
        car_showroom_id=car_showroom.user.id, provider_id=provider.user.id
    )

    assert discount.discount_rate == first_purchase_discount


@pytest.mark.django_db
def test_provider_discount_no_discount(
    create_user_provider, create_user_car_showroom, create_provider
):
    user_provider = create_user_provider()
    user_car_showroom = create_user_car_showroom()
    provider = create_provider(user=user_provider)
    car_showroom = CarShowRoomFactory(user=user_car_showroom)
    no_discount = get_provider_discount_for_special_client(
        car_showroom_id=car_showroom.user.id, provider_id=provider.user.id
    )

    assert no_discount == 0


@pytest.mark.django_db
def test_provider_discount_regular_discount(
    create_user_provider,
    create_user_car_showroom,
    create_provider,
    create_regular_customer_discount,
):
    user_provider = create_user_provider()
    user_car_showroom = create_user_car_showroom()
    provider = create_provider(user=user_provider)
    car_showroom = CarShowRoomFactory(user=user_car_showroom)
    discount = create_regular_customer_discount(provider_discount=provider)
    with patch("car_showroom.models.SellModel.objects.filter") as mock_filter:
        mock_filter.return_value.count.return_value = 201
        regular_discount = get_provider_discount_for_special_client(
            car_showroom_id=car_showroom.user.id, provider_id=provider.user.id
        )

    assert discount.discount_rate == regular_discount
