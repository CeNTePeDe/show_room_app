from datetime import date

import pytest
from unittest.mock import patch
from core.car_showroom_discount import (
    get_season_discount_from_car_showroom,
    get_car_showroom_discount_for_special_client,
)
from customer.tests.factories import CustomerFactory


@pytest.mark.django_db
def test_get_season_discount_from_car_showroom(
    create_car_showroom, create_season_discount, create_user_car_showroom
):
    user = create_user_car_showroom()
    car_showroom = create_car_showroom(user=user)
    discount = create_season_discount(car_showroom_discount=car_showroom)
    season_discount = get_season_discount_from_car_showroom(
        sale_date=date.today(), car_showroom_id=car_showroom.user.id
    )

    assert season_discount == discount.discount_rate


@pytest.mark.django_db
def test_get_season_discount_from_car_showroom_no_discount(
    create_car_showroom, create_user_car_showroom
):
    user = create_user_car_showroom()
    car_showroom = create_car_showroom(user=user)
    car_showroom_id = car_showroom.user.id
    season_discount = get_season_discount_from_car_showroom(
        sale_date=date.today(), car_showroom_id=car_showroom_id
    )

    assert season_discount == 0


@pytest.mark.django_db
def test_car_showroom_discount_for_first_purchase(
    create_car_showroom,
    create_user_car_showroom,
    create_user_customer,
    create_first_purchase_discount,
):
    user_customer = create_user_customer()
    user_car_showroom = create_user_car_showroom()
    customer = CustomerFactory(user=user_customer)
    car_showroom = create_car_showroom(user=user_car_showroom)
    discount = create_first_purchase_discount(car_showroom_discount=car_showroom)
    first_purchase_discount = get_car_showroom_discount_for_special_client(
        car_showroom_id=car_showroom.user.id, customer_id=customer.user.id
    )

    assert discount.discount_rate == first_purchase_discount


@pytest.mark.django_db
def test_car_showroom_discount_no_discount(
    create_user_customer, create_user_car_showroom, create_car_showroom
):
    user_customer = create_user_customer()
    user_car_showroom = create_user_car_showroom()
    customer = CustomerFactory(user=user_customer)
    car_showroom = create_car_showroom(user=user_car_showroom)
    no_discount = get_car_showroom_discount_for_special_client(
        car_showroom_id=car_showroom.user.id, customer_id=customer.user.id
    )

    assert no_discount == 0


@pytest.mark.django_db
def test_car_showroom_discount_regular_customer(
    create_car_showroom,
    create_user_car_showroom,
    create_user_customer,
    create_regular_customer_discount,
):
    user_customer = create_user_customer()
    user_car_showroom = create_user_car_showroom()
    customer = CustomerFactory(user=user_customer)
    car_showroom = create_car_showroom(user=user_car_showroom)
    discount = create_regular_customer_discount(car_showroom_discount=car_showroom)
    with patch("customer.models.Transaction.objects.filter") as mock_filter:
        mock_filter.return_value.count.return_value = 5
        regular_discount = get_car_showroom_discount_for_special_client(
            car_showroom_id=car_showroom.user.id, customer_id=customer.user.id
        )

    assert discount.discount_rate == regular_discount
