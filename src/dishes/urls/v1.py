from rest_framework.routers import DefaultRouter
from dishes.views import (
   CategoryViewSet,
   SetViewSet,
   GroupViewSet,
   DishViewSet
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"sets", SetViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"dishes", DishViewSet)

urlpatterns = router.urls
