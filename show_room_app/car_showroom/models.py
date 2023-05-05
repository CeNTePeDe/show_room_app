from django.db import models
from djmoney.models.fields import MoneyField

from core.abstract_models import BaseRole, BaseSellModel


class CarShowRoom(BaseRole):
    cars = models.ManyToManyField("cars.Car", through="SellModel")
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car_ShowRoom"


class SellModel(BaseSellModel):
    car_showroom = models.ForeignKey(
        "car_showroom.CarShowRoom", on_delete=models.CASCADE
    )
    car = models.ForeignKey("cars.Car", on_delete=models.CASCADE)
    provider = models.ForeignKey("provider.Provider", on_delete=models.CASCADE)

    discount = models.ForeignKey("discount.ProviderDiscount", on_delete=models.CASCADE)
    season_discount = models.ForeignKey(
        "discount.SeasonDiscount", on_delete=models.CASCADE
    )
