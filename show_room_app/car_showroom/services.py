import django_filters
from .models import SellModel


class CarFromCarShowRoomFilter(django_filters.FilterSet):
    car_showroom = django_filters.CharFilter(field_name="car_showroom__name")
    car = django_filters.CharFilter(field_name="car__name")

    class Meta:
        model = SellModel
        fields = ["car_showroom", "car"]
