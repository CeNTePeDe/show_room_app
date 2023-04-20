from django.db import models
from djmoney.forms import MoneyField

from core.abstract_models import BaseRole, MiddleModel


class CarShowRoom(BaseRole):
    provider = models.ManyToManyField(
        "provider.Provider", through="ProviderCarShowRoom"
    )
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)

    balance = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "Car_ShowRoom"


class ProviderCarShowRoom(MiddleModel):
    provider = models.ForeignKey("provider.Provider", on_delete=models.CASCADE)
    car_showroom = models.ForeignKey(
        "car_showroom.CarShowRoom", on_delete=models.CASCADE
    )

    discount = models.ForeignKey(
        "discount.CarShowRoomDiscount", on_delete=models.CASCADE
    )
    season_discount = models.ForeignKey(
        "discount.TemporaryDiscount", on_delete=models.CASCADE
    )
