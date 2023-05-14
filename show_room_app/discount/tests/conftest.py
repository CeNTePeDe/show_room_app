import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register
from discount.tests.factories import (
    SeasonDiscountFactory,
    ProviderDiscountFactory,
    CarShowRoomDiscountFactory,
)

register(SeasonDiscountFactory)
register(ProviderDiscountFactory)
register(CarShowRoomDiscountFactory)


@pytest.fixture
def api_client():
    client = APIClient()
    return client
