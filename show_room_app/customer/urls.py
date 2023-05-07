from rest_framework.routers import DefaultRouter

from customer.views import CustomerView, TransactionView

router = DefaultRouter()

router.register(r"customer", CustomerView, basename="customer")
router.register(r"transaction", TransactionView, basename="transaction")

urlpatterns = router.urls
