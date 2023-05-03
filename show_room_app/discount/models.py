from django.core.validators import MaxValueValidator
from django.db import models

from core.abstract_models import BaseDiscount


class ProviderDiscount(BaseDiscount):
    discount_rate = models.PositiveIntegerField(
        verbose_name="Provider discount",
        validators=[MaxValueValidator(100)],
        default=30,
        help_text="in per cent",
    )


class CarShowRoomDiscount(BaseDiscount):
    discount_rate = models.PositiveIntegerField(
        verbose_name="Car Showroom discount",
        validators=[MaxValueValidator(100)],
        default=20,
        help_text="in per cent",
    )


class SeasonDiscount(models.Model):
    discount_name = models.CharField(
        max_length=50,
    )
    date_start = models.DateField(
        blank=False,
        null=False,
    )
    date_finish = models.DateField(
        blank=False,
        null=False,
    )
    discount_rate = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        default=0,
        help_text="in per cent",
    )

    def __str__(self):
        return self.discount_name
