from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from user.managers import CustomUserManager


class User(AbstractUser):
    is_customer = models.BooleanField(_("customer"), default=False)
    is_car_showroom = models.BooleanField(_("car_showroom"), default=False)
    is_provider = models.BooleanField(_("provider"), default=False)
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    Manager = CustomUserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
