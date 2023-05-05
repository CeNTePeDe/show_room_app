from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

from cars.choice import BodyType, EnginType, NumberOfDoor, Color
from core.validators_show_room import validate_year


class Car(models.Model):
    """This model describe Car."""

    name = models.CharField(max_length=40)
    model_car = models.CharField(max_length=40)
    image = models.ImageField(
        upload_to="car_images", null=True, blank=True, verbose_name="car"
    )
    year = models.PositiveSmallIntegerField(
        null=True, blank=True, validators=[validate_year]
    )
    country = CountryField(blank=False)
    created_at = models.DateField(auto_now_add=True)
    body_type = models.CharField(
        max_length=25,
        choices=BodyType.choices,
        default=BodyType.Sedan,
    )
    color = models.CharField(
        max_length=25,
        choices=Color.choices,
        default=Color.Emerald,
    )
    engine_type = models.CharField(
        max_length=25, choices=EnginType.choices, default=EnginType.Petrol
    )
    number_of_doors = models.CharField(
        max_length=25, choices=NumberOfDoor.choices, default=NumberOfDoor.FourDoor
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.model_car}"

    class Meta:
        verbose_name = "Car"
