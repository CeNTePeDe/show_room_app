import pytest
from .factories import UserFactory

#
# @pytest.fixture()
# def build_user_customer():
#     def user(**kwargs):
#         return UserFactory.build(username="customer1", is_customer=True, **kwargs)
#
#     return user
#
#
# @pytest.fixture()
# def build_user_car_showroom():
#     def user(**kwargs):
#         return UserFactory.build(is_car_showroom=True, **kwargs)
#
#     return user
#
#
# @pytest.fixture()
# def build_user_provider():
#     def user(**kwargs):
#         return UserFactory.build(username="provider1", is_provider=True, **kwargs)
#
#     return user
