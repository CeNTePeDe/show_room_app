from datetime import date
from collections import Counter

from celery import shared_task
from django.db.models import Q

from core.services import get_provider_discount, get_season_discount, get_final_provider_price
from provider.models import CarProvider, Provider
from car_showroom.models import CarShowRoom, SellModel


@shared_task()
def buy_car_from_provider(user_id):
    characteristic = CarShowRoom.objects.get(user_id=user_id).characteristic
    car_providers = CarProvider.objects.filter(
        Q(car__color=characteristic["color"])
        | Q(car__body_type=characteristic["body_type"])
        | Q(car__engine_type=characteristic["engine_type"])
        | Q(car__number_of_doors=characteristic["number_of_doors"])
    )

    for provider in car_providers:

        sell_model = SellModel.objects.create(
            car_showroom=CarShowRoom.objects.get(user_id=user_id),
            car=provider.car,
            provider=provider.provider,
            discount=get_provider_discount(provider_id=provider.provider.user_id, car_showroom_id=user_id),
            season_discount=get_season_discount(sale_day=date.today()),

        )
        sell_model.save()
