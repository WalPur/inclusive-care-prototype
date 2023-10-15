from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from care.models import (
    Article,
    CenterRating,
    Event,
    EventRegistration,
    ReabilatationCenter,
    Tag,
)
from care.serializers import (
    ArticleSerializer,
    EventRegistrationSerializer,
    EventSerializer,
    RatingSerializer,
    ReabilitationListSerializer,
    ReabilitationRetrieveSerializer,
    TagSerializer,
)


class CenterViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = ReabilatationCenter.objects.all()

    @action(methods=["post"], detail=True, serializer_class=RatingSerializer)
    def rate(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {
            "user": request.user,
            "center": self.get_object(),
            **serializer.validated_data,
        }
        if CenterRating.objects.filter(**data).exists():
            raise ValidationError("Вы уже поставили отзыв")
        else:
            CenterRating.objects.create(**data)
            return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "rate":
            return RatingSerializer
        if self.action != "list":
            return ReabilitationRetrieveSerializer
        return ReabilitationListSerializer


class ArticleViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TagViewSet(
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class EventViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(methods=["post"], detail=True, serializer_class=EventRegistrationSerializer)
    def register(self, request, *args, **kwargs):
        if EventRegistration.objects.filter(
            user=request.user, event=self.get_object()
        ).exists():
            raise ValidationError("Вы уже зарегистрированы на событие")
        else:
            serializer = EventRegistrationSerializer(
                EventRegistration.objects.create(
                    user=request.user, event=self.get_object()
                )
            )
            return Response(serializer.data)
