import jwt

from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from show_room_app import settings
from .managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    is_customer = models.BooleanField(default=False)
    is_car_showroom = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    Manager = CustomUserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
