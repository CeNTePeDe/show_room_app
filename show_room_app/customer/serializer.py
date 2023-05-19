from rest_framework import serializers

from car_showroom.serializer import CarShowRoomSerializer
from customer.models import Customer, Transaction
from discount.serializer import CarShowRoomDiscountSerializer, SeasonDiscountSerializer


class TransactionSerializer(serializers.ModelSerializer):
    car_showroom = CarShowRoomSerializer()
    discount = CarShowRoomDiscountSerializer()
    season_discount = SeasonDiscountSerializer()

    class Meta:
        model = Transaction
        fields = ("car_showroom", "price", "date", "discount", "season_discount")


class CustomerSerializer(serializers.ModelSerializer):
    purchases = TransactionSerializer()

    class Meta:
        model = Customer
        fields = ("user", "username", "balance", "purchases", "max_price", "is_active")
