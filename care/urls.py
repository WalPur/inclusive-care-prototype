from django.urls import include, path
from rest_framework.routers import DefaultRouter

from care.views import CenterViewSet

router = DefaultRouter()
router.register("centers", CenterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
