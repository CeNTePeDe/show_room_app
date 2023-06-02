from datetime import date

from car_showroom.models import SellModel
from discount.models import ProviderDiscount
from provider.models import Provider


def get_season_discount_from_provider(sale_date, provider_id):
    """
    The function get season_discount for car_showroom.
    Parameters:
        sale_date (date): Date when car_showroom buys cars
        provider_id (int): Id provider

    Returns:
        discount_rate (int): Discount_rate for particular car_showroom.

    """
    provider = Provider.objects.get(user_id=provider_id)
    try:
        provider.discounts.get(
            date_start__lte=sale_date, date_finish__gte=sale_date, is_active=True
        )
        return provider.discounts.get(
            discount_name="season_discount", is_active=True
        ).discount_rate
    except ProviderDiscount.DoesNotExist:
        return 0


def get_provider_discount_for_special_client(provider_id, car_showroom_id):
    """
    The function get special discount for regular customer(car_showroom)
    and discount for first purchase.
    Parameters:
        car_showroom_id (int): Id car_showroom.
        provider_id (int): Id provider.

    Returns:
        discount_rate (int): Discount_rate for special customer(car_showroom).

    """
    provider = Provider.objects.get(user_id=provider_id)
    count_car_showroom = SellModel.objects.filter(
        provider=provider_id, car_showroom=car_showroom_id
    ).count()

    if count_car_showroom == 0:
        return provider.discounts.get(
            discount_name="first_purchase_discount", is_active=True
        ).discount_rate

    elif count_car_showroom > 200:
        return provider.discounts.get(
            discount_name="regular_customer", is_active=True
        ).discount_rate
    else:
        return provider.discounts.get(
            discount_name="no_discount", is_active=True
        ).discount_rate


def get_full_discount(provider_id: int, car_showroom_id: int) -> float:
    """
    The function calculates full discount from provider.
    Parameters:
        car_showroom_id (int): Id car_showroom.
        provider_id (int): Id provider.

    Returns:
        discount (float): Discount.

    """
    discount = (
        get_season_discount_from_provider(
            sale_date=date.today(), provider_id=provider_id
        )
        + get_provider_discount_for_special_client(
            provider_id=provider_id, car_showroom_id=car_showroom_id
        )
    ) / 100

    return discount
