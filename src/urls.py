from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

swagger_urls = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

api_urls = [
    path("api/v1/users/", include("users.urls")),
    path("api/v1/care/", include("care.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += swagger_urls
urlpatterns += api_urls
