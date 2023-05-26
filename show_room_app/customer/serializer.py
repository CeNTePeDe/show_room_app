from rest_framework import serializers

from car_showroom.serializer import CarShowRoomSerializer
from cars.serializer import CarSerializer
from customer.models import Customer, Transaction
from discount.serializer import CarShowRoomDiscountSerializer, SeasonDiscountSerializer
from user.models import User
from user.serializer import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Customer
        fields = ("user", "username", "balance", "characteristic_car", "is_active")
        read_only_fields = ("balance",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)

        return customer


class TransactionSerializer(serializers.ModelSerializer):
    # car_showroom = CarShowRoomSerializer()
    # discount = CarShowRoomDiscountSerializer()
    # season_discount = SeasonDiscountSerializer()
    # car = CarSerializer()

    class Meta:
        model = Transaction
        fields = (
            "car_showroom",
            "car",
            "price",
            "date",
            "discount",
            "season_discount",
        )
