from datetime import date

import pytest
from core.car_showroom_discount import get_season_discount_from_car_showroom


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
