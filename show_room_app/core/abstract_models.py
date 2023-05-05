from django.core.validators import MaxValueValidator
from django.db import models
from django_countries.fields import CountryField
from django.db.models import JSONField

from core.default_value import jsonfield_default_value
from core.validators_show_room import validate_year


class BaseDiscount(models.Model):
    """Abstract model for discount."""

    discount_name = models.CharField(max_length=30)
    discount_rate = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        default=0,
        help_text="in per cent",
    )

    def __str__(self):
        return self.discount_name

    class Meta:
        abstract = True


class BaseRole(models.Model):
    name = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(
        null=True, blank=True, validators=[validate_year]
    )

    country = CountryField(default="Russia")
    characteristic = JSONField(default=jsonfield_default_value)
    data_add = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class BaseSellModel(models.Model):
    """The model describes intermediate models with ManyToMany relationship."""

    margin = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        default=0,
        help_text="in per cent",
    )
    number_of_cars = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
