from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField
from django.db.models import JSONField

from core.validators_show_room import validate_year
from core.default_value import jsonfield_default_value


class BaseDiscount(models.Model):
    """
    abstract model for discount
    """

    discount_name = models.CharField(max_length=30, verbose_name="discount name")
    discount_rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name="discount rate",
        help_text="in per cent",
    )

    class Meta:
        abstract = True


class BaseRole(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    year = models.IntegerField(
        validators=[validate_year], default=datetime.now().year, verbose_name="year"
    )
    country = CountryField(default="Russia", blank=False)
    characteristic = JSONField(default=jsonfield_default_value)
    data_add = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class MiddleModel(models.Model):
    margin = models.IntegerField(
        verbose_name="margin",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        help_text="in per cent",
    )
    number_of_cars = models.IntegerField(
        verbose_name="number of cars", validators=[MinValueValidator(0)], default=0
    )

    def get_total_price(self, price):
        total_price = float((price * self.margin) / 100)
        return total_price

    class Meta:
        abstract = True
