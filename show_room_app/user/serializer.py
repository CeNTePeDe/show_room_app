from rest_framework import serializers
from user.models import User


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)

    is_customer = serializers.BooleanField(required=False)
    is_provider = serializers.BooleanField(required=False)
    is_car_showroom = serializers.BooleanField(required=False)

    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "is_customer",
            "is_provider",
            "is_car_showroom",
            "is_active",
        ]
