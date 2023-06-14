from django.db import models

from core.abstract_models import BaseRole, BaseSellModel


class Provider(BaseRole):
    """
    The model describes provider characteristic.
    """

    cars = models.ManyToManyField(
        "cars.Car",
        through="CarProvider",
    )
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="provider",
        limit_choices_to={"is_provider": True},
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Provider"


class CarProvider(BaseSellModel):
    """
    The model describes which cars the provider sells.
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

    def __str__(self):
        return self.provider.name
