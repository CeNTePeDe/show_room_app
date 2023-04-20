from django.db import models
from djmoney.forms import MoneyField


class Customer(models.Model):
    """
    This model describes Customer and connections with model CarShowRoom
    """

    username = models.CharField(max_length=40)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    purchases = models.ForeignKey("Transaction", on_delete=models.CASCADE)
    max_price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    is_active = models.BooleanField(default=True)

    def __repr__(self):
        return self.username

    class Meta:
        verbose_name = "Customer"


class Transaction(models.Model):
    car_showroom = models.ForeignKey(
        "car_showroom.CarShowRoom", on_delete=models.CASCADE
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    date = models.DateField(auto_now_add=True)
    discount = models.ForeignKey("discount.ProviderDiscount", on_delete=models.CASCADE)
    season_discount = models.ForeignKey(
        "discount.TemporaryDiscount", on_delete=models.CASCADE
    )
