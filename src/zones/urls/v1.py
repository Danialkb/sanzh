from rest_framework.routers import DefaultRouter

from zones.views import ZoneViewSet, TableViewSet

router = DefaultRouter()

router.register("zones", ZoneViewSet)
router.register("tables", TableViewSet)

urlpatterns = router.urls
