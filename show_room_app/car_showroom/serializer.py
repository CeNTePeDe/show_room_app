from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from car_showroom.models import CarShowRoom, SellModel


class CarShowRoomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    # cars = serializers.StringRelatedField(many=True, read_only=True)
    # user = serializers.CharField(source="user.username")

    class Meta:
        model = CarShowRoom
        fields = (
            "name",
            "year",
            "country",
            "characteristic",
            "data_add",
            "balance",
            "user",
            "cars",
            "is_active",
        )


class SellModelSerializer(serializers.ModelSerializer):
    # car_showroom = serializers.CharField(source="car_showroom.name")
    # discount = serializers.CharField(source="discount.discount_name")
    # season_discount = serializers.StringRelatedField(source="discount.discount_name")
    # provider = serializers.CharField(source="provider.name")
    # car = serializers.CharField(source="car.name")

    class Meta:
        model = SellModel
        fields = (
            "car_showroom",
            "car",
            "provider",
            "discount",
            "season_discount",
            "margin",
            "number_of_cars",
        )
