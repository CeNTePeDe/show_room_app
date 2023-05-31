from django.db import models

from core.abstract_models import BaseDiscount


class ProviderDiscount(BaseDiscount):
    provider = models.ForeignKey(
        "provider.CarProvider",
        related_name="discounts",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )


class CarShowRoomDiscount(BaseDiscount):
    car_showroom = models.ForeignKey(
        "car_showroom.SellModel",
        related_name="discounts",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
