from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from car_showroom.models import CarShowRoom, SellModel
from cars.models import Car
from cars.serializer import CarSerializer
from discount.models import CarShowRoomDiscount, ProviderDiscount
from discount.serializer import CarShowRoomDiscountSerializer
from provider.models import Provider
from provider.serializer import ProviderSerializer
from user.models import User
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
        user = User.objects.create(**user_data)
        car_showroom = CarShowRoom.objects.create(user=user, **validated_data)

        return car_showroom


class SellModelSerializer(serializers.ModelSerializer):
    car_showroom = CarShowRoomSerializer(required=False, read_only=True)
    provider = ProviderSerializer(required=False, read_only=True)
    discount = CarShowRoomDiscountSerializer(required=False, read_only=True)

    car = CarSerializer(required=False, read_only=True)

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
