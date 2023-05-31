from rest_framework import serializers

from discount.models import ProviderDiscount, CarShowRoomDiscount


class ProviderDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderDiscount
        fields = "__all__"


class CarShowRoomDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShowRoomDiscount
        fields = "__all__"
