from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)

    is_customer = serializers.BooleanField(required=False)
    is_provider = serializers.BooleanField(required=False)
    is_car_showroom = serializers.BooleanField(required=False)

    password = serializers.CharField(required=True, write_only=True)
    password_confirm = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password_confirm",
            "email",
            "first_name",
            "last_name",
            "is_customer",
            "is_provider",
            "is_car_showroom",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            is_customer=validated_data["is_customer"],
            is_provider=validated_data["is_provider"],
            is_car_showroom=validated_data["is_car_showroom"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "is_customer",
            "is_provider",
            "is_car_showroom",
        ]
