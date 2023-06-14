from rest_framework import serializers

from car_showroom.models import CarShowRoom
from cars.models import Car
from customer.models import Customer, Transaction


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("user", "username", "balance", "model_car", "is_active")


class TransactionSerializer(serializers.ModelSerializer):
    car_showroom = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=CarShowRoom.objects.all()
    )

    customer = serializers.SlugRelatedField(
        many=False, slug_field="username", queryset=Customer.objects.all()
    )
    car = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=Car.objects.all()
    )

    class Meta:
        model = Transaction
        fields = (
            "car",
            "customer",
            "car_showroom",
            "price",
            "date",
        )
