from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.mixins import (
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import CustomUser
from users.serializers import UserRegistrationSerializer, UserSerializer


class UserViewSet(
    GenericViewSet,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):
    serializer_class = UserSerializer
    # queryset = CustomUser.objects.all()

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        if self.request.user.is_staff is False:
            return self.request.user
        return queryset

    def get_permissions(self):
        if self.action in ["register", "login"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(methods=["post"], detail=False, serializer_class=UserRegistrationSerializer)
    def register(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        CustomUser.objects.create_user(**serializer.data)
        return Response(serializer.data)

    @action(methods=["post"], detail=False, serializer_class=AuthTokenSerializer)
    def login(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
            }
        )
