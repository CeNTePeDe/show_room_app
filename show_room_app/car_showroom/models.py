from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField
from djmoney.forms import MoneyField
from django.db.models import JSONField

from core.default_value import jsonfield_default_value
from core.validators_show_room import validate_year


class CarShowRoom(models.Model):
    name = models.CharField(max_length=30, verbose_name="Car show_room")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    year = models.IntegerField(
        validators=[validate_year], default=datetime.now().year, verbose_name="year"
    )
    country = CountryField(default="England", blank=False)
    provider = models.ManyToManyField(
        "provider.Provider", through="ProviderCarShowRoom"
    )
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    characteristic = JSONField(default=jsonfield_default_value)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    is_active = models.BooleanField(default=True)

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "Car_ShowRoom"


class ProviderCarShowRoom(models.Model):
    provider = models.ForeignKey("provider.Provider", on_delete=models.CASCADE)
    car_showroom = models.ForeignKey(
        "car_showroom.CarShowRoom", on_delete=models.CASCADE
    )
    margin = models.DecimalField(max_digits=3, decimal_places=2)
    number_of_car = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    discount = models.ForeignKey(
        "discount.CarShowRoomDiscount", on_delete=models.CASCADE
    )
