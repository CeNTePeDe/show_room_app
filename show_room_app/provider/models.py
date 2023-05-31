from django.db import models

from core.abstract_models import BaseRole, BaseSellModel


class Provider(BaseRole):
    cars = models.ManyToManyField(
        "cars.Car",
        through="CarProvider",
    )
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, primary_key=True, related_name="provider"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Provider"


class CarProvider(BaseSellModel):
    """
    This model is describing relationship Car-Provider,
    and add number of car with margin(rate).
    """

    car = models.ForeignKey(
        "cars.Car",
        related_name="car",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )
    provider = models.ForeignKey(
        "provider.Provider",
        related_name="provider",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )

    @property
    def provider_price(self):
        margin_amount = self.car.price * (self.margin / 100)
        return self.car.price + margin_amount
