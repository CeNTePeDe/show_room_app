from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from car_showroom.models import CarShowRoom, SellModel


class CarShowRoomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = CarShowRoom
        fields = ("name", "year", "country")


class CarShowRoomDetailSerializer(serializers.ModelSerializer):
    cars = serializers.StringRelatedField(many=True)

    class Meta:
        model = CarShowRoom
        fields = (
            "name",
            "year",
            "country",
            "characteristic",
            "data_add",
            "cars",
            "is_active",
            "user",
        )


class SellModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellModel
        fields = (
            "car_showroom",
            "car",
            "provider",
            "discount",
            "season_discount",
        )
