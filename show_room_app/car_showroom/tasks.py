from celery import shared_task
from django.db.models import Q

from core.provider_discount import get_full_discount
from provider.models import CarProvider
from car_showroom.models import CarShowRoom, SellModel


@shared_task()
def buy_car_from_provider(user_id: int) -> None:
    car_showroom = CarShowRoom.objects.get(user_id=user_id)
    list_of_cars = car_showroom.list_cars_to_buy["cars"]
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
            # calculate discount
            discount = get_full_discount(
                provider_id=car_item.provider.user.id, car_showroom_id=user_id
            )

            price = car_item.provider_price * discount + car_item.provider_price
            # add similar car to one dictionary car_with_price
            car_with_price.update({car_item: price})

        # get min price for car
        car_min_price = min(car_with_price.items(), key=lambda x: x[1])
        car_provider, price_provider = car_min_price

        # get balance showroom
        balance_car_showroom = car_showroom.balance.amount

        if price_provider.amount * car["count"] < balance_car_showroom:
            SellModel.objects.create(
                car_showroom=car_showroom,
                car=car_provider.car,
                provider=car_provider.provider,
                count=car["count"],
                price_provider=price_provider,
            )
            # change balance CarShowRoom after purchase
            car_showroom.balance = (
                balance_car_showroom - price_provider.amount * car["count"]
            )
            car_showroom.save()


@shared_task()
def buy_car_from_provider_for_each_car_showroom() -> None:
    user_ids = CarShowRoom.objects.values_list("user_id", flat=True)
    for user_id in user_ids:
        buy_car_from_provider.delay(user_id)
