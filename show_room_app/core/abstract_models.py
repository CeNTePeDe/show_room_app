from django.db import models


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
