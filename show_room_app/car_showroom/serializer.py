from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from car_showroom.models import CarShowRoom, SellModel
from cars.serializer import CarSerializer
from discount.serializer import SeasonDiscountSerializer, CarShowRoomDiscountSerializer
from provider.serializer import ProviderSerializer
from user.serializer import UserSerializer


class CarShowRoomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    user = UserSerializer(required=False)

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

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.save()
        car_showroom = CarShowRoom.objects.create(user=user, **validated_data)
        car_showroom.save()

        return car_showroom


class SellModelSerializer(serializers.ModelSerializer):
    # car_showroom = CarShowRoomSerializer()
    # discount = CarShowRoomDiscountSerializer()
    # season_discount = SeasonDiscountSerializer()
    # provider = ProviderSerializer()
    # car = CarSerializer()

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
