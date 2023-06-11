import pytest

from customer.models import Transaction
from customer.tasks import matching_car_for_customer, purchase_marching_car_for_customer


@pytest.mark.django_db
def test_matching_car_for_customer_no_suitable_car(
    create_customer, create_user_customer
):
    user = create_user_customer()
    customer = create_customer(user=user)
    sell_model = matching_car_for_customer(user_id=customer.id)

    assert sell_model is None


@pytest.mark.django_db
def test_matching_car_for_customer(
    create_customer, create_user_customer, create_sell_model_for_tasks
):
    user = create_user_customer()
    customer = create_customer(
        user=user, model_car={"name": "Test", "model": "car", "price": 0.0, "count": 1}
    )
    sell_model = create_sell_model_for_tasks()
    matching_car = matching_car_for_customer(user_id=customer.user.id)

    assert len(matching_car) == 1


@pytest.mark.django_db
def test_matching_car_for_customer_no_car(
    create_customer, create_user_customer, create_sell_model_for_tasks
):
    user = create_user_customer()
    customer = create_customer(
        user=user, model_car={"name": "Test", "model": "test", "price": 0.0, "count":1}
    )
    sell_model = create_sell_model_for_tasks()
    matching_car = matching_car_for_customer(user_id=customer.user.id)

    assert matching_car is None


@pytest.mark.django_db
def test_purchase_marching_car_for_customer(
    create_sell_model_for_tasks, create_user_customer, create_customer
):
    sell_model = create_sell_model_for_tasks()
    car_showroom = sell_model.car_showroom

    user = create_user_customer()
    customer = create_customer(
        user=user,
        model_car={"name": "Test", "model": "car", "price": 11000, "count":1},
        balance="20000.0",
    )

    purchase_marching_car_for_customer(user_id=customer.user.id)
    transaction = Transaction.objects.first()

    assert Transaction.objects.count() == 1
    assert transaction.customer == customer
    assert transaction.car_showroom == car_showroom
    assert transaction.car == sell_model.car
