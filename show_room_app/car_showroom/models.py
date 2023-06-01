from django.db import models
from djmoney.models.fields import MoneyField

from core.abstract_models import BaseRole, BaseSellModel
from core.constants import jsonfield_car_showroom


class CarShowRoom(BaseRole):
    """
    Model describes CarShowRoom with characteristic for car.
    """

    cars = models.ManyToManyField("cars.Car", through="SellModel")
    characteristic = models.JSONField(default=jsonfield_car_showroom)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="car_showroom",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car_ShowRoom"


class SellModel(BaseSellModel):
    """
    Model describes what cars showroom sells.
    """

    car_showroom = models.ForeignKey(
        "car_showroom.CarShowRoom",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )
    car = models.ForeignKey("cars.Car", on_delete=models.CASCADE)
    provider = models.ForeignKey(
        "provider.Provider",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )
    date = models.DateField(auto_now_add=True)
    count = models.PositiveIntegerField(default=1)
    price_provider = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")

    @property
    def price(self):
        margin_amount = self.price_provider * (self.margin / 100)
        return self.price_provider + margin_amount
