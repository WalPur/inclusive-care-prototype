from django.urls import path

from users.views import UserAuthView

urlpatterns = [
    path("login", UserAuthView.as_view()),
]
