from django.contrib import admin

from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from car_showroom.views import CarShowRoomListView
from cars.views import CarListView
from customer.views import CustomerView, TransactionView
from provider.views import ProviderListView, CarProviderListView
from discount.views import (
    SeasonDiscountView,
    ProviderDiscountView,
    CarShowRoomDiscountView,
)
from user.views import UserView

router = DefaultRouter()
router.register(r"user", UserView, basename="user")
router.register(r"cars", CarListView, basename="car")
router.register(r"provider", ProviderListView, basename="provider")
router.register(r'car_provider', CarProviderListView, basename="car_provider")
router.register(r"car_showroom", CarShowRoomListView, basename="car_showroom")
router.register(r"customer", CustomerView, basename="customer")
router.register(r"transaction", TransactionView, basename="transaction")
router.register(r"season_discount", SeasonDiscountView, basename="season_discount")
router.register(
    r"provider_discount", ProviderDiscountView, basename="provider_discount"
)
router.register(
    r"car_showroom_discount", CarShowRoomDiscountView, basename="car_showroom_discount"
)


schema_view = get_schema_view(
    openapi.Info(
        title="Car Show Room API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@CarShowRoom.local"),
        license=openapi.License(name="BSD License"),
    ),
    patterns=[
        path("api/v1/", include(router.urls)),
    ],
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swaggerui/swaggerui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("admin/", admin.site.urls),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
    path("api/v1/", include(router.urls)),
   # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
