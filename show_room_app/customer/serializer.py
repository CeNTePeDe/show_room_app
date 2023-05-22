from rest_framework import serializers

from car_showroom.serializer import CarShowRoomSerializer
from customer.models import Customer, Transaction
from discount.serializer import CarShowRoomDiscountSerializer, SeasonDiscountSerializer
from user.models import User
from user.serializer import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Customer
        fields = ("user", "username", "balance", "max_price", "is_active")

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.save()
        customer = Customer.objects.create(user=user, **validated_data)
        customer.save()
        return customer


class TransactionSerializer(serializers.ModelSerializer):
    car_showroom = CarShowRoomSerializer()
    discount = CarShowRoomDiscountSerializer()
    season_discount = SeasonDiscountSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Transaction
        fields = (
            "car_showroom",
            "customer",
            "price",
            "date",
            "discount",
            "season_discount",
        )
