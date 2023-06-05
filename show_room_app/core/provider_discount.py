from datetime import date

from car_showroom.models import SellModel
from discount.models import ProviderDiscount
from provider.models import Provider


def get_season_discount_from_provider(sale_date: date, provider_id: int) -> int:
    provider = Provider.objects.get(user_id=provider_id)
    try:
        season_discount = provider.discounts.get(
            date_start__lte=sale_date, date_finish__gte=sale_date, is_active=True
        ).discount_rate
        return season_discount
    except ProviderDiscount.DoesNotExist:
        return 0


def get_provider_discount_for_special_client(
    provider_id: int, car_showroom_id: int
) -> int:
    provider = Provider.objects.get(user_id=provider_id)
    count_car_showroom = SellModel.objects.filter(
        provider=provider_id, car_showroom=car_showroom_id
    ).count()

    if count_car_showroom == 0:
        try:
            first_purchase_discount = provider.discounts.get(
                discount_name="first_purchase_discount", is_active=True
            ).discount_rate
            return first_purchase_discount
        except ProviderDiscount.DoesNotExist:
            return 0

    elif count_car_showroom > 200:
        try:
            regular_customer = provider.discounts.get(
                discount_name="regular_customer", is_active=True
            ).discount_rate
            return regular_customer
        except ProviderDiscount.DoesNotExist:
            return 0
    return 0


def get_full_discount(provider_id: int, car_showroom_id: int) -> float:
    season_discount = get_season_discount_from_provider(
        sale_date=date.today(), provider_id=provider_id
    )
    provider_discount = get_provider_discount_for_special_client(
        provider_id=provider_id, car_showroom_id=car_showroom_id
    )
    discount = (season_discount + provider_discount) / 100

    return discount
