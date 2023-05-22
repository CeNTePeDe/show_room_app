from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import (
    UserView,
    RegistrationAPIView,
    ChangePasswordView,
    UserAPI,
    UserLogoutAPIView,
    UserLoginAPIView,
)

router = DefaultRouter()
router.register(r"user", UserView, basename="user")


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegistrationAPIView.as_view(), name="create-user"),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout-user"),
    path("change_password/", ChangePasswordView.as_view(), name="change-password"),
    # path("user/", UserAPI.as_view({'get': 'list'}), name="user"),
]
