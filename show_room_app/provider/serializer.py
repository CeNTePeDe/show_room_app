from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from cars.serializer import CarSerializer
from provider.models import Provider, CarProvider
from user.models import User
from user.serializer import UserSerializer


class ProviderSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    user = UserSerializer(required=False)

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

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.save()
        provider = Provider.objects.create(user=user, **validated_data)
        provider.save()
        return provider


class CarProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarProvider
        fields = (
            "provider",
            "car",
            "number_of_cars",
            "margin",
        )
