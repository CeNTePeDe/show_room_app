from datetime import date
import pytest
from core.provider_discount import get_season_discount_from_provider


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
def test_get_season_discount_from_car_showroom_no_discount(
    create_provider, create_user_provider
):
    user = create_user_provider()
    provider = create_provider(user=user)
    provider_id = provider.user.id
    season_discount = get_season_discount_from_provider(
        sale_date=date.today(), provider_id=provider_id
    )

    assert season_discount == 0
