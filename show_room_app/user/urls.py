from django.urls import path
from rest_framework.routers import DefaultRouter


from user.views import (
    UserView,
    RegistrationAPIView,
    ActivateView,
    ForgotPasswordView,
    UserLoginAPIView,
    ResetPasswordView,
    UserLogoutAPIView,
)

router = DefaultRouter()
router.register(r"user", UserView, basename="user")


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("activate/<str:uidb64>/<str:token>/", ActivateView.as_view(), name="activate"),
    path("forgot_password/", ForgotPasswordView.as_view(), name="forgot_password"),
    path(
        "reset_password/<str:uidb64>/<str:token>/",
        ResetPasswordView.as_view(),
        name="reset_password",
    ),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout-user"),
]
