from car_showroom.models import SellModel
from discount.models import ProviderDiscount
from provider.models import Provider


def get_season_discount_from_provider(sale_day, provider_id):
    provider = Provider.objects.get(user_id=provider_id)
    try:
        provider.discounts.filter(is_active=True).get(
            date_start__lte=sale_day, date_finish__gte=sale_day
        )
        return (
            provider.discounts.filter(is_active=True)
            .get(discount_name="season_discount")
            .discount_rate
        )
    except ProviderDiscount.DoesNotExist:
        return provider.discounts.get(discount_name="no_discount").discount_rate


def get_provider_discount_for_special_client(provider_id, car_showroom_id):
    provider = Provider.objects.get(user_id=provider_id)
    count_car_showroom = SellModel.objects.filter(
        provider=provider_id, car_showroom=car_showroom_id
    ).count()
    try:
        if count_car_showroom == 0:
            return (
                provider.discounts.filter(is_active=True)
                .get(discount_name="first_purchase_discount")
                .discount_rate
            )
        elif 0 < count_car_showroom < 200:
            return (
                provider.discounts.filter(is_active=True)
                .get(discount_name="no_discount")
                .discount_rate
            )
        return (
            ProviderDiscount.objects.filter(is_active=True)
            .get(discount_name="regular_customer")
            .discount_rate
        )
    except ProviderDiscount.DoesNotExist:
        return provider.discounts.get(discount_name="no_discount").discount_rate


def get_provider_discount():
    pass


def discount_for_special_client():
    pass


def discount_for_special_customer():
    pass


def season_discount():
    pass
