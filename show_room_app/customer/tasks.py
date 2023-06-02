from decimal import Decimal

from celery import shared_task
from django.db.models import Q

from car_showroom.models import SellModel
from core.car_showroom_discount import get_full_discount
from customer.models import Customer, Transaction


@shared_task()
def buy_car_from_car_showroom(user_id):
    """
    Task for buying the most suitable car for customer from car_showroom
    according to characteristic_car from customer
    Parameters:
        user_id(int): Id customer
    Returns:
        None
    """
    customer = Customer.objects.get(user_id=user_id)
    model_car = customer.characteristic_car

    filter_for_model_car = Q(car__name=model_car["name"]) & Q(
        car__model_car=model_car["model"]
    )
    sell_model = SellModel.objects.filter(filter_for_model_car)
    car_with_price: dict = {}
    for car_item in sell_model:
        price = (
            car_item.price
            * get_full_discount(
                car_showroom_id=car_item.car_showroom_id, customer_id=user_id
            )
            + car_item.price
        )
        car_with_price.update({car_item: price})

        car_min_price = min(car_with_price.items(), key=lambda x: x[1])
        # balance customer
        customer_balance = customer.balance.amount

        # car_showroom
        car_showroom = car_min_price[0].car_showroom

        if car_min_price[1].amount < Decimal(model_car["price"]):
            Transaction.objects.create(
                car=car_min_price[0].car,
                customer=customer,
                car_showroom=car_showroom,
                price=car_min_price[1].amount,
            )
            customer.balance = customer_balance - car_min_price[1].amount
            customer.save()

            # add price_car to car_showroom balance
            car_showroom.balance += car_min_price[1].amount
