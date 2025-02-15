from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet, OrderItemViewSet

router = DefaultRouter()

router.register(r"orders", OrderViewSet)
router.register(r"orders_items", OrderItemViewSet)

urlpatterns = router.urls
