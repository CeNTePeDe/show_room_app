from rest_framework.routers import DefaultRouter

from cars.views import CarView

router = DefaultRouter()
router.register(r"cars", CarView, basename="car")
urlpatterns = router.urls
