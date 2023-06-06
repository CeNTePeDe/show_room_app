from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "is_customer",
            "is_provider",
            "is_car_showroom",
        )


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """

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
            password=validated_data["password"],
            password_confirm=validated_data["password_confirm"],
            is_customer=validated_data["is_customer"],
            is_provider=validated_data["is_provider"],
            is_car_showroom=validated_data["is_car_showroom"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    """
    Serializer class to authenticate users with email and password.
    """

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

    class Meta:
        model = User
        fields = ("username", "email", "password")


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("password", "password_confirm")

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.set_password(validated_data["password_confirm"])
        instance.save()

        return instance


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ("email",)


class TokenPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user,
        }
