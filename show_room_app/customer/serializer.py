from rest_framework import serializers

from customer.models import Customer, Transaction


class CustomerSerializer(serializers.ModelSerializer):
    purchases = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = ("user", "username", "balance", "purchases", "max_price")


class TransactionSerializer(serializers.ModelSerializer):
    car_showroom = serializers.StringRelatedField(read_only=True)
    discount = serializers.StringRelatedField(read_only=True)
    season_discount = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = ("car_showroom", "price", "date", "discount", "season_discount")
