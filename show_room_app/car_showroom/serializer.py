from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

from car_showroom.models import CarShowRoom, SellModel
from cars.models import Car
from cars.serializer import CarSerializer
from discount.models import CarShowRoomDiscount, SeasonDiscount, ProviderDiscount
from discount.serializer import SeasonDiscountSerializer, CarShowRoomDiscountSerializer
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
    # many=True, выпадает ошибка, что объект не является итерируемым
    car_showroom = CarShowRoomSerializer(required=False, read_only=True)
    provider = ProviderSerializer(required=False, read_only=True)
    discount = CarShowRoomDiscountSerializer(required=False, read_only=True)
    season_discount = SeasonDiscountSerializer(required=False, read_only=True)
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

    # def create(self, validated_data):
    #     car_data = validated_data.pop("car")
    #     car = Car.objects.create(**car_data)
    #
    #     discount_data = validated_data.pop("discount")
    #     discount = ProviderDiscount.objects.create(**discount_data)
    #
    #     season_discount_data = validated_data.pop("season_discount")
    #     season_discount = SeasonDiscount.objects.create(**season_discount_data)
    #
    #     car_showroom_data = validated_data.pop("car_showroom")
    #     car_showroom_user_data = car_showroom_data.pop("user")
    #     user_car_showroom = User.objects.create(**car_showroom_user_data)
    #     car_showroom = CarShowRoom.objects.create(user=user_car_showroom, **car_showroom_data)
    #
    #     provider_data = validated_data.pop("provider")
    #     provider_user_data = provider_data.pop("user")
    #     user_provider = User.objects.create(**provider_user_data)
    #     provider = Provider.objects.create(user=user_provider, **provider_data)
    #
    #     sell_model = SellModel.objects.create(car_showroom=car_showroom,
    #                                           car=car,
    #                                           provider=provider,
    #                                           discount=discount,
    #                                           season_discount=season_discount,
    #                                           **validated_data)
    #     return sell_model
    #
