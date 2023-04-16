import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField
from django.db.models import JSONField

from core.default_value import jsonfield_default_value
from core.validators_show_room import validate_year


class Provider(models.Model):
    name_company = models.CharField(max_length=40, verbose_name="provider")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    year = models.IntegerField(
        validators=[validate_year],
        default=datetime.datetime.now().year,
        verbose_name="year",
    )
    cars = models.ManyToManyField("cars.Car", through="CarProvider")
    country = CountryField(default="England", blank=False)
    characteristic = JSONField(default=jsonfield_default_value)
    is_active = models.BooleanField(default=True)

    def __repr__(self):
        return self.name_company

    class Meta:
        verbose_name = "Provider"


class CarProvider(models.Model):
    """this model is describing relationship Car-Provider, and add number of car
    with margin(rate)"""

    car = models.ForeignKey("cars.Car", on_delete=models.CASCADE)
    provider = models.ForeignKey("provider.Provider", on_delete=models.CASCADE)
    margin = models.DecimalField(max_digits=3, decimal_places=2)
    number_of_cars = models.IntegerField(
        verbose_name="number of cars", validators=[MinValueValidator(0)], default=0
    )
