from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from cars.serializer import CarSerializer
from provider.models import Provider, CarProvider
from user.models import User
from user.serializer import UserSerializer


class ProviderSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    # user = UserSerializer(required=False)

    class Meta:
        model = Provider
        fields = (
            "name",
            "year",
            "country",
            "cars",
            "user",
            "data_add",
            "is_active",
        )

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        provider = Provider.objects.create(user=user, **validated_data)
        return provider


class CarProviderSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = CarProvider
        fields = (
            "provider",
            "car",
            "margin",
        )
