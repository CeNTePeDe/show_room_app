from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from cars.models import Car


class CarSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """List of cars"""

    class Meta:
        model = Car
        fields = "__all__"
