from datetime import date

from celery import shared_task
from django.db.models import Q, Min

from cars.models import Car
from core.services import (
    get_season_discount_from_provider,
    get_provider_discount_for_special_client,
)
from provider.models import CarProvider, Provider
from car_showroom.models import CarShowRoom, SellModel


@shared_task()
def buy_car_from_provider(user_id):
    list_of_cars = CarShowRoom.objects.get(user_id=user_id).characteristic["cars"]

    for car in list_of_cars:
        filter_for_car = (
            Q(car__name=car["name"]) & Q(car__model_car=car["model_car"])
            | Q(car__color=car["color"])
            | Q(car__body_type=car["body_type"])
            | Q(car__engine_type=car["engine_type"])
            | Q(car__number_of_doors=car["number_of_doors"])
        )

        car_provider = CarProvider.objects.filter(filter_for_car)
        car_with_price: dict = {}
        for car_item in car_provider:
            price = (
                car_item.provider_price
                * (
                    get_season_discount_from_provider(
                        sale_day=date.today(), provider_id=car_item.provider_id
                    )
                    + get_provider_discount_for_special_client(
                        provider_id=car_item.provider_id, car_showroom_id=user_id
                    )
                )
                / 100
                + car_item.provider_price
            )
            # add similar car in to one dictionary car_with_price
            car_with_price.update({car_item: price})
        # get min price for car
        car_min_price = min(car_with_price.items(), key=lambda x: x[1])

        balance_car_showroom = CarShowRoom.objects.get(user_id=user_id).balance.amount

        if car_min_price[1].amount * car["count"] < balance_car_showroom:
            SellModel.objects.create(
                car_showroom=CarShowRoom.objects.get(user_id=user_id),
                car=Car.objects.get(id=car_min_price[0].car.id),
                provider=Provider.objects.get(user_id=car_min_price[0].provider.user_id),
                count=car["count"],
                price_provider=car_min_price[1],
            )
                    # change balance CarShowRoom after purchase
            CarShowRoom.objects.filter(user_id=user_id).update(
                balance=(
                    balance_car_showroom - car_min_price[1].amount * car["count"]
                )
            )
