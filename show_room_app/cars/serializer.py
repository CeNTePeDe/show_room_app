from rest_framework import serializers

from cars.models import Car


class CarListSerializers(serializers.ModelSerializer):
    """List of cars"""

    class Meta:
        model = Car
        fields = ("name", "model_car", "created_at")


class CarDitailSerializer(serializers.ModelSerializer):
    """List ditail cars"""

    class Meta:
        model = Car
        exclude = ("slug", "price", "is_active")


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
