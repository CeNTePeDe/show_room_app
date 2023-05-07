from rest_framework.routers import DefaultRouter

from provider.views import ProviderView, CarProviderListView

router = DefaultRouter()
router.register(r"provider", ProviderView, basename="provider")
router.register(r"car_provider", CarProviderListView, basename="car_provider")

urlpatterns = router.urls
