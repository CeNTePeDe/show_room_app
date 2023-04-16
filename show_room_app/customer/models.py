from django.db import models
from djmoney.forms import MoneyField
from django.contrib.postgres.fields import ArrayField


class Customer(models.Model):
    """
    This model describes Customer and connections with model CarShowRoom
    """

    username = models.CharField(max_length=40)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    # историю покупок заносим в list_of_purchases
    list_of_purchases = ArrayField(models.CharField(max_length=200), blank=True)
    # для того чтобы покупатель вводил макс сумму за авто
    max_price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    # для поиска определенной модели
    cars = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
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
