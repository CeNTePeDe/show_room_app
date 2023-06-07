from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from car_showroom.models import CarShowRoom, SellModel
from cars.models import Car
from cars.serializer import CarSerializer
from provider.models import Provider


class CarShowRoomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = CarShowRoom
        fields = (
            "name",
            "year",
            "country",
            "balance",
            "list_cars_to_buy",
            "data_add",
            "user",
            "is_active",
        )


class SellModelSerializer(serializers.ModelSerializer):
    car_showroom = serializers.SlugRelatedField(
        queryset=CarShowRoom.objects.all(), many=False, slug_field="name"
    )
    provider = serializers.SlugRelatedField(
        queryset=Provider.objects.all(),
        many=False,
        slug_field="name",
    )
    car = CarSerializer()

    class Meta:
        model = SellModel
        fields = (
            "car_showroom",
            "car",
            "margin",
            "count",
            "provider",
        )

    def create(self, validated_data):
        car_data = validated_data.pop("car")
        car = Car.objects.create(**car_data)
        sell_model = SellModel.objects.create(car=car, **validated_data)

        return sell_model

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
