from datetime import date
from car_showroom.models import SellModel, CarShowRoom
from discount.models import SeasonDiscount, ProviderDiscount, CarShowRoomDiscount
from provider.models import CarProvider


def get_season_discount(sale_day):
    try:
        season_discount = SeasonDiscount.objects.get(date_start__lte=sale_day, date_finish__gte=sale_day)
        return season_discount
    except SeasonDiscount.DoesNotExist:
        return SeasonDiscount.objects.get(discount_name="no_discount")


def get_provider_discount(provider_id, car_showroom_id):
    count_car_showroom = SellModel.objects.filter(provider=provider_id, car_showroom=car_showroom_id).count()
    if count_car_showroom == 0:
        return ProviderDiscount.objects.get(discount_name='first_purchase_discount')
    elif 0 < count_car_showroom < 200:
        return ProviderDiscount.objects.get(discount_name='no_discount')
    return ProviderDiscount.objects.get(discount_name='regular_customer')


def get_final_provider_price(provider_id, car_showroom_id):
    cars = CarProvider.objects.get(provider=provider_id)
    for car_price in cars.provider_price:
        final_provider_price = (get_provider_discount(provider_id, car_showroom_id).discount_rate + get_season_discount(
            sale_day=date.today()).discount_rate)/100*car_price + car_price
        return final_provider_price


def get_car_showroom_discount():
    pass
