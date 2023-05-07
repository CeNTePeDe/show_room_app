from django.urls import include, path
from rest_framework.routers import DefaultRouter

from user.views import UserView, RegistrationAPIView

router = DefaultRouter()
router.register(r"user", UserView, basename="user")
urlpatterns = [
    path("", include(router.urls)),
    path("create/", RegistrationAPIView.as_view()),
]
