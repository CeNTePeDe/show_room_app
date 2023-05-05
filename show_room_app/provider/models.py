from django.db import models

from core.abstract_models import BaseRole, BaseSellModel


class Provider(BaseRole):
    cars = models.ManyToManyField("cars.Car", through="CarProvider")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Provider"


class CarProvider(BaseSellModel):
    """
    This model is describing relationship Car-Provider,
    and add number of car with margin(rate).
    """

    car = models.ForeignKey("cars.Car", on_delete=models.CASCADE)
    provider = models.ForeignKey("provider.Provider", on_delete=models.CASCADE)
