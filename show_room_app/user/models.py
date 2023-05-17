import jwt

from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .managers import CustomUserManager


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_car_showroom = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    password_confirm = models.CharField(max_length=30, default="1111")
    Manager = CustomUserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
