from django.core.validators import MaxValueValidator
from django.db import models
from django_countries.fields import CountryField

from core.validators import validate_year


class BaseDiscount(models.Model):
    """Abstract model for discount."""

    discount_name = models.CharField(max_length=30)
    discount_rate = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        default=0,
        help_text="in per cent",
    )
    date_start = models.DateField(
        blank=True,
        null=True,
    )
    date_finish = models.DateField(
        blank=True,
        null=True,
    )
    special_discount = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.discount_name

    class Meta:
        abstract = True


class BaseRole(models.Model):
    """Absctarct model describes base role in app."""

    name = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(
        null=True, blank=True, validators=[validate_year]
    )

    country = CountryField(default="Russia")
    data_add = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class BaseSellModel(models.Model):
    """
    The model describes intermediate models with ManyToMany relationship.
    """

    margin = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        default=10,
        help_text="in per cent",
    )

    class Meta:
        abstract = True
