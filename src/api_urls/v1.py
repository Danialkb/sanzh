from django.urls import path, include

urlpatterns = [
    path("", include("users.urls.v1")),
    path("", include("zones.urls.v1")),
    path("", include("departments.urls.v1")),
    path("", include("dishes.urls.v1")),
    path("", include("orders.urls.v1")),
]
