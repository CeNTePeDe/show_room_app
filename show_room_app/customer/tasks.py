from decimal import Decimal

from celery import shared_task
from django.db.models import Q
from django.db.models import QuerySet

from car_showroom.models import SellModel
from core.car_showroom_discount import get_full_discount
from core.constants import jsonfield_customer
from customer.models import Transaction, Customer


def matching_car_for_customer(user_id: int) -> QuerySet[SellModel]:
    """
    Find the most suitable car for customer.
    """
    # retrieve object customer
    customer = Customer.objects.get(user_id=user_id)
    model_car = customer.model_car

    filter_for_model_car = Q(car__name=model_car["name"]) & Q(
        car__model_car=model_car["model"]
    )
    sell_model = SellModel.objects.filter(filter_for_model_car).filter(
        count__gte=model_car["count"]
    )
    if len(sell_model) >= 1:
        return sell_model


def find_car_with_min_price(sell_model: QuerySet[SellModel], user_id: int) -> tuple:
    car_with_price: dict = {}
    for car_item in sell_model:
        discount = get_full_discount(
            car_showroom_id=car_item.car_showroom.user.id, customer_id=user_id
        )
        price = car_item.price * discount + car_item.price
        car_with_price.update({car_item: price})

    car_min_price = min(car_with_price.items(), key=lambda x: x[1])
    return car_min_price


def purchase_marching_car_for_customer(user_id: int) -> None:
    customer = Customer.objects.get(user_id=user_id)
    car_models = matching_car_for_customer(user_id=user_id)
    if car_models:
        sell_model, car_price = find_car_with_min_price(
            sell_model=car_models, user_id=user_id
        )
        # balance customer
        customer_balance = customer.balance.amount
        # car_showroom
        car_showroom = sell_model.car_showroom

        if car_price.amount < Decimal(customer.model_car["price"]):
            Transaction.objects.create(
                car=sell_model.car,
                customer=customer,
                car_showroom=car_showroom,
                price=car_price.amount,
            )
            # calculate balance and clean field model_car
            customer.balance = customer_balance - car_price.amount
            customer.model_car = jsonfield_customer()
            customer.save()
            # add price_car to car_showroom balance
            car_showroom.balance.amount += car_price.amount
            car_showroom.save()
            # remove car from sell_model
            sell_model.count = sell_model.count - 1
            sell_model.save()


@shared_task()
def buy_car_from_car_showroom(user_id: int) -> None:
    purchase_marching_car_for_customer(user_id)
