from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.abstract_models import BaseDiscount


class ProviderDiscount(BaseDiscount):
    discount_rate = models.IntegerField(
        verbose_name="discount",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=30,
        help_text="in per cent",
    )


class CarShowRoomDiscount(BaseDiscount):
    discount_rate = models.IntegerField(
        verbose_name="discount",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=20,
        help_text="in per cent",
    )


class TemporaryDiscount(BaseDiscount):
    date_start = models.DateField(auto_now=True)
    date_finish = models.DateField(auto_now=True)
    discount_rate = models.IntegerField(
        verbose_name="discount",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        help_text="in per cent",
    )
    data_transaction = models.DateField(auto_now_add=True)

    def get_price(self, price):
        if self.date_start < self.data_transaction < self.date_finish:
            total_price = float((price * self.discount_rate) / 100)
            return total_price
        else:
            return price
