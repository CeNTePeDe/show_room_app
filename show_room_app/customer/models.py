from decimal import Decimal

from django.db import models
from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField
from djmoney.models.validators import MinMoneyValidator

from core.constants import jsonfield_customer


class Customer(models.Model):
    """
    The model describes Customer and connections with model CarShowRoom.
    """

    username = models.CharField(max_length=40)
    balance = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency="USD",
        null=True,
    )
    model_car = JSONField(default=jsonfield_customer, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="customer",
        limit_choices_to={"is_customer": True},
    )

    def __str__(self):
        return self.username

    def clean(self):
        if Decimal(self.model_car["price"]) >= self.balance.amount:
            raise ValidationError(_("Max price cannot be greater than balance."))

    class Meta:
        verbose_name = "Customer"


class Transaction(models.Model):
    """
    The model describes which cars were bought.
    """

    car = models.ForeignKey(
        "cars.Car", on_delete=models.CASCADE, limit_choices_to={"is_active": True}
    )
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    car_showroom = models.ForeignKey(
        "car_showroom.CarShowRoom",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.car_showroom.name

    class Meta:
        verbose_name = "Transaction"
