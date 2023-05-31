from celery import shared_task
from django.db.models import Q, Min

from provider.models import CarProvider
from car_showroom.models import CarShowRoom


@shared_task()
def buy_car_from_provider(user_id):
    list_of_cars = CarShowRoom.objects.get(user_id=user_id).characteristic.cars

    for car in list_of_cars:
        filter_by_car = (
            Q(car__name=car["name"]) & Q(car__model_car=car["model_car"])
            | Q(car__color=car["color"])
            | Q(car__body_type=car["body_type"])
            | Q(car__engine_type=car["engine_type"])
            | Q(car__number_of_doors=car["number_of_doors"])
        )
        car_provider = CarProvider.objects.filter(filter_by_car).aggregate(
            price=Min("CarProvider.provider_price")
        )
