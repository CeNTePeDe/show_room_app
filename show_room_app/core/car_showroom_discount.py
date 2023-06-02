from datetime import date

from car_showroom.models import CarShowRoom
from customer.models import Transaction
from discount.models import CarShowRoomDiscount


def get_season_discount_from_car_showroom(sale_date: date, car_showroom_id: int) -> int:
    car_showroom = CarShowRoom.objects.get(user_id=car_showroom_id)
    try:
        season_discount = car_showroom.discounts.get(
            date_start__lte=sale_date, date_finish__gte=sale_date, is_active=True
        ).discount_rate
        return season_discount
    except CarShowRoomDiscount.DoesNotExist:
        return 0



def get_car_showroom_discount_for_special_client(
    car_showroom_id: int, customer_id: int
) -> int:
    car_showroom = CarShowRoom.objects.get(user_id=car_showroom_id)
    count_car_customer = Transaction.objects.filter(
        customer=customer_id, car_showroom=car_showroom_id
    ).count()

    if count_car_customer == 0:
        try:
            first_purchase_discount = car_showroom.discounts.get(
                discount_name="first_purchase_discount", is_active=True
            ).discount_rate
            return first_purchase_discount
        except CarShowRoomDiscount.DoesNotExist:
            return 0

    elif count_car_customer > 4:
        try:
            regular_customer = car_showroom.discounts.get(
                discount_name="regular_customer", is_active=True
            ).discount_rate
            return regular_customer
        except CarShowRoomDiscount.DoesNotExist:
            return 0
    return 0


def get_full_discount(car_showroom_id: int, customer_id: int) -> float:
    season_discount = get_season_discount_from_car_showroom(
        sale_date=date.today(), car_showroom_id=car_showroom_id
    )

    car_showroom_discount = get_car_showroom_discount_for_special_client(
        car_showroom_id=car_showroom_id, customer_id=customer_id
    )

    discount = (season_discount + car_showroom_discount) / 100

    return discount
