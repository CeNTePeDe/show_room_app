from rest_framework.routers import DefaultRouter

from discount.views import (
    SeasonDiscountView,
    ProviderDiscountView,
    CarShowRoomDiscountView,
)

router = DefaultRouter()

router.register(r"season_discount", SeasonDiscountView, basename="season_discount")
router.register(
    r"provider_discount", ProviderDiscountView, basename="provider_discount"
)
router.register(
    r"car_showroom_discount", CarShowRoomDiscountView, basename="car_showroom_discount"
)

urlpatterns = router.urls
