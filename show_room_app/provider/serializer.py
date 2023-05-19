from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from cars.serializer import CarSerializer
from provider.models import Provider, CarProvider
from user.serializer import UserSerializer


class ProviderSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    user = UserSerializer()

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


class CarProviderSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    provider = ProviderSerializer()

    class Meta:
        model = CarProvider
        fields = (
            "provider",
            "car",
            "number_of_cars",
            "margin",
        )
