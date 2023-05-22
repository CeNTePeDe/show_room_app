from django.db import models
from djmoney.models.fields import MoneyField


class Customer(models.Model):
    """
    This model describes Customer and connections with model CarShowRoom.
    """

    username = models.CharField(max_length=40)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    max_price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(
        "user.User", on_delete=models.CASCADE, primary_key=True, related_name="customer"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Customer"


class Transaction(models.Model):
    car_showroom = models.ForeignKey(
        "car_showroom.CarShowRoom", on_delete=models.CASCADE
    )
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    date = models.DateField(auto_now_add=True)
    discount = models.ForeignKey(
        "discount.CarShowRoomDiscount", on_delete=models.CASCADE
    )
    season_discount = models.ForeignKey(
        "discount.SeasonDiscount", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.car_showroom.name

    class Meta:
        verbose_name = "Transaction"
