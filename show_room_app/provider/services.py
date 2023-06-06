import django_filters
from provider.models import CarProvider


class CarProviderFilter(django_filters.FilterSet):
    provider = django_filters.CharFilter(field_name="provider__name")
    car = django_filters.CharFilter(field_name="car__name")

    class Meta:
        model = CarProvider
        fields = ("provider", "car")
