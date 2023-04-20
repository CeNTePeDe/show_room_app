from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

from cars.choice import (
    CHOICES_BODY_TYPE,
    CHOICES_ENGINE_TYPE,
    CHOICES_COLOR,
    CHOICES_NUMBER_OF_DOORS,
)


class Car(models.Model):
    """This model describe Car"""

    name = models.CharField(max_length=40, verbose_name="name car")
    model_car = models.CharField(max_length=40, verbose_name="name of the model")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    image = models.ImageField(
        upload_to="car_images", null=True, blank=True, verbose_name="car"
    )
    country = CountryField(default="England", blank=False)
    created_at = models.DateField(auto_now_add=True)
    body_type = models.CharField(
        max_length=3, choices=CHOICES_BODY_TYPE, verbose_name="body type", default="s"
    )
    color = models.CharField(
        max_length=20, verbose_name="color", choices=CHOICES_COLOR, default="129"
    )
    engine_type = models.CharField(
        max_length=1, choices=CHOICES_ENGINE_TYPE, default="p"
    )
    number_of_doors = models.CharField(
        max_length=1, choices=CHOICES_NUMBER_OF_DOORS, default="4"
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    is_active = models.BooleanField(default=True)

    def __repr__(self):
        return f"{self.name},{self.model_car}"

    class Meta:
        verbose_name = "Car"
