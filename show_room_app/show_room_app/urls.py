from django.contrib import admin

from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


from show_room_app import settings

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
        path("api/v1_car/", include("cars.urls")),
        path("api/v1_provider/", include("provider.urls")),
        path("api/v1_car_showroom/", include("car_showroom.urls")),
        path("api/v1_customer/", include("customer.urls")),
        path("api/v1_discount/", include("discount.urls")),
        path("api/v1_user/", include("user.urls")),
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
    path("api/v1_car/", include("cars.urls")),
    path("api/v1_provider/", include("provider.urls")),
    path("api/v1_car_showroom/", include("car_showroom.urls")),
    path("api/v1_customer/", include("customer.urls")),
    path("api/v1_discount/", include("discount.urls")),
    path("api/v1_user/", include("user.urls")),
]
if settings.DEBUG:
    urlpatterns = [path("__debug__/", include("debug_toolbar.urls"))] + urlpatterns
