from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from provider.models import Provider, CarProvider


class ProviderSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("name", "year", "country", "characteristic")


class CarProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarProvider
        fields = (
            "provider",
            "number_of_cars",
            "margin",
            "car",
        )


class ProviderDetailSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Provider
        fields = ("name", "year", "country", "characteristic", "cars", "user")
