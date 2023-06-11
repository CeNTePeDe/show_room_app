import pytest
from celery.contrib.testing.worker import start_worker
from django.conf import settings

from show_room_app.celery import app as celery_app


@pytest.fixture(scope="session")
def celery_worker():
    worker = start_worker(celery_app)
    return worker


@pytest.fixture(scope="session")
def celery_app(request):
    return celery_app


@pytest.fixture(scope="session")
def celery_config():
    return {
        "broker_url": settings.CELERY_BROKER_URL,
        "result_backend": settings.CELERY_RESULT_BACKEND,
    }


from customer.tasks import buy_car_from_car_showroom


@pytest.mark.django_db
def test_celery_worker(celery_worker, create_user_customer, create_customer):
    user = create_user_customer()
    customer = create_customer(user=user)

    print(f"Customer ID: {customer.id}")
    result = buy_car_from_car_showroom.delay(customer.user.id)
    print(f"Task result: {result.get()}")
    assert result.get() == "success"


