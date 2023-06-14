import django_filters
from customer.models import Transaction


class TransactionFilter(django_filters.FilterSet):
    customer = django_filters.CharFilter(field_name="customer__username")
    car_showroom = django_filters.CharFilter(field_name="car_showroom__name")
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Transaction
        fields = ["customer", "car_showroom", "date"]
