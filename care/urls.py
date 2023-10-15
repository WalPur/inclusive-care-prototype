from django.urls import include, path
from rest_framework.routers import DefaultRouter

from care.views import ArticleViewSet, CenterViewSet, EventViewSet, TagViewSet

router = DefaultRouter()
router.register("centers", CenterViewSet)
router.register("articles", ArticleViewSet)
router.register("tags", TagViewSet)
router.register("events", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
