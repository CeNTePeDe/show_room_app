from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from cars.models import Car
from cars.serializer import CarSerializer
from provider.models import Provider, CarProvider


class ProviderSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

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


class CarProviderSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    provider = serializers.SlugRelatedField(
        queryset=Provider.objects.all(),
        many=False,
        slug_field="name",
    )

    class Meta:
        model = CarProvider
        fields = (
            "provider",
            "car",
            "margin",
        )

    def create(self, validated_data):
        car_data = validated_data.pop("car")
        car = Car.objects.create(**car_data)
        car_provider = CarProvider.objects.create(car=car, **validated_data)

        return car_provider

    def update(self, instance, validated_data):
        car_data = validated_data.pop("car", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if car_data is not None:
            car_instance = instance.car
            for key, value in car_data.items():
                setattr(car_instance, key, value)
            car_instance.save()
        instance.save()
        return instance
