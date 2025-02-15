from rest_framework.routers import DefaultRouter

from departments.views import KitchenDepartmentViewSet

router = DefaultRouter()

router.register(r"kitchen-departments", KitchenDepartmentViewSet)

urlpatterns = router.urls
