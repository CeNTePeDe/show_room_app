from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False, verbose_name="customer")
    is_car_showroom = models.BooleanField(default=False, verbose_name="car_showroom")
    is_provider = models.BooleanField(default=False, verbose_name="provider")
