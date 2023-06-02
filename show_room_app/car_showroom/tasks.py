from celery import shared_task
from django.db.models import Q

from core.provider_discount import get_full_discount
from provider.models import CarProvider
from car_showroom.models import CarShowRoom, SellModel


@shared_task()
def buy_car_from_provider(user_id):
    """
    Task for buying the cheapest cars for car_showroom from provider
    according to list_of_car from car_showroom.
    Parameters:
        user_id (int): Id car_showroom.
    Returns:
        None
    """
    car_showroom = CarShowRoom.objects.get(user_id=user_id)
    list_of_cars = car_showroom.list_of_car_model["cars"]
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
                * get_full_discount(
                    provider_id=car_item.provider_id, car_showroom_id=user_id
                )
                + car_item.provider_price
            )
            # add similar car to one dictionary car_with_price
            car_with_price.update({car_item: price})
        # get min price for car
        car_min_price = min(car_with_price.items(), key=lambda x: x[1])
        # get balance showroom
        balance_car_showroom = car_showroom.balance.amount

        if car_min_price[1].amount * car["count"] < balance_car_showroom:
            SellModel.objects.create(
                car_showroom=car_showroom,
                car=car_min_price[0].car,
                provider=car_min_price[0].provider,
                count=car["count"],
                price_provider=car_min_price[1],
            )
            # change balance CarShowRoom after purchase
            car_showroom.balance = (
                balance_car_showroom - car_min_price[1].amount * car["count"]
            )
            car_showroom.save()
