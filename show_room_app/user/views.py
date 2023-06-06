from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import (
    get_object_or_404,
    GenericAPIView,
    CreateAPIView,
)
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from cars.permission import IsAdminUserOrReadOnly
from show_room_app import settings
from user.models import User
from user.serializer import (
    UserSerializer,
    UserRegistrationSerializer,
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    UserLoginSerializer,
)


class UserView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class RegistrationAPIView(CreateAPIView):
    """
    An endpoint for the client to create a new User.
    """

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        subject = "Activate Your Account"
        message = render_to_string(
            "registration/activation_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            },
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])


class ActivateView(APIView):
    """
    APIView for activate user instance.
    """

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"status": "activated"})
        else:
            return Response(
                {"status": "invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )


class ForgotPasswordView(GenericAPIView):
    """
    Endpoint for change password according to user's email
    """

    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        email = request.data.get("email")
        user = get_object_or_404(User, email=email)
        current_site = get_current_site(request)
        subject = "Reset Your Password"
        message = render_to_string(
            "registration/reset_password_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            },
        )
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
        return Response({"status": "email sent"})


class ResetPasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            password = request.data.get("password")
            user.set_password(password)
            user.save()
            return Response({"status": "password reset"})
        else:
            return Response(
                {"status": "invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = UserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
