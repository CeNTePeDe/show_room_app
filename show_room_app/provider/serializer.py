from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from provider.models import Provider, CarProvider


class CarProviderSerializer(serializers.ModelSerializer):
    car = serializers.CharField(source="car.name")
    provider = serializers.CharField(source="provider.name")

    class Meta:
        model = CarProvider
        fields = (
            "provider",
            "number_of_cars",
            "margin",
            "car",
        )


class ProviderSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = serializers.StringRelatedField(many=True, read_only=True)
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Provider
        fields = (
            "name",
            "year",
            "country",
            "characteristic",
            "cars",
            "user",
            "is_active",
        )
