from rest_framework.routers import DefaultRouter

from car_showroom.views import CarShowRoomView, SellModelView

router = DefaultRouter()
router.register(r"car_showroom", CarShowRoomView, basename="car_showroom")
router.register(r"sell_car", SellModelView, basename="sell_car")

urlpatterns = router.urls
