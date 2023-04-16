from django.db import models

from core.abstract_models import BaseDiscount


class ProviderDiscount(BaseDiscount):
    discount_rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.3)


class CarShowRoomDiscount(BaseDiscount):
    discount_rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.2)
