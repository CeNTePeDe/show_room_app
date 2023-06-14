from django.db import models

from core.abstract_models import BaseDiscount


class ProviderDiscount(BaseDiscount):
    provider_discount = models.ForeignKey(
        "provider.Provider",
        related_name="discounts",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )


class CarShowRoomDiscount(BaseDiscount):
    car_showroom_discount = models.ForeignKey(
        "car_showroom.CarShowRoom",
        related_name="discounts",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
