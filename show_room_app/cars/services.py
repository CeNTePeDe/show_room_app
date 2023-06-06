import django_filters
from cars.models import Car


class CarFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Car
        fields = {
            "name": ["istartswith"],
            "model_car": ["istartswith"],
            "price": ["lt", "gt"],
            "body_type": ["exact"],
        }
