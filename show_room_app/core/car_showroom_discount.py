from datetime import date

from car_showroom.models import CarShowRoom
from customer.models import Transaction
from discount.models import CarShowRoomDiscount


def get_season_discount_from_car_showroom(sale_date, car_showroom_id):
    """
    The function get season_discount for customer
    Parameters:
        sale_date(date): Date when customer buys car.
        car_showroom_id(int): Id car_showroom.

    Returns:
        discount_rate(int): Discount_rate for particular customer
    """
    car_showroom = CarShowRoom.objects.get(user_id=car_showroom_id)
    try:
        return car_showroom.discounts.get(
            date_start__lte=sale_date, date_finish__gte=sale_date, is_active=True
        ).discount_rate

    except CarShowRoomDiscount.DoesNotExist:
        return 0


def get_car_showroom_discount_for_special_client(car_showroom_id, customer_id):
    """
    The function get special discount for regular customer from car_showroom.
    Parameters:
        car_showroom_id(int): Id car_showroom.
        customer_id(int): Id customer.
    Returns:
        discount_rate(int): Discount_rate for special customer.

    """
    car_showroom = CarShowRoom.objects.get(user_id=car_showroom_id)
    count_car_customer = Transaction.objects.filter(
        customer=customer_id, car_showroom=car_showroom_id
    ).count()
    try:
        if count_car_customer == 0:
            return car_showroom.discounts.get(
                discount_name="first_purchase_discount", is_active=True
            ).discount_rate
        elif 0 > count_car_customer < 2:
            return 0
        elif count_car_customer > 2:
            return car_showroom.discounts.get(
                discount_name="regular_customer", is_active=True
            ).discount_rate
    except CarShowRoomDiscount.DoesNotExist:
        return 0


def get_full_discount(car_showroom_id, customer_id):
    """
    The function calculate full discount from car_showroom.
    Parameters:
        car_showroom_id (int): Id car_showroom.
        customer_id (int): Id customer.

    Returns:
        discount(float): Full discount.

    """
    discount = (
        get_season_discount_from_car_showroom(
            sale_date=date.today(), car_showroom_id=car_showroom_id
        )
        + get_car_showroom_discount_for_special_client(
            car_showroom_id=car_showroom_id, customer_id=customer_id
        )
    ) / 100
    return discount
