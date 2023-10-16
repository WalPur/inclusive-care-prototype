from django.db import models

from care.choices import SpecialisationChoices
from users.models import ContactData, CustomUser


class ReabilatationCenter(models.Model):
    name = models.TextField("Название")
    contact_data = models.ForeignKey(
        ContactData, models.SET_NULL, related_name="centers", null=True
    )
    description = models.TextField("Описание предоставляемых услуг")
    schedule = models.TextField("Расписание работы")
    specialisation = models.CharField(
        "Специализация", max_length=16, choices=SpecialisationChoices.choices
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Реабилитационный центр"
        verbose_name_plural = "Реабилитационные центры"


class CenterRating(models.Model):
    user = models.ForeignKey(
        CustomUser, models.SET_NULL, null=True, related_name="ratings"
    )
    center = models.ForeignKey(
        ReabilatationCenter, models.SET_NULL, null=True, related_name="ratings"
    )
    rating = models.IntegerField("Оценка")
    text = models.TextField("Отзыв", blank=True)
    date = models.DateTimeField("Дата оценки", auto_now_add=True)

    def __str__(self) -> str:
        return "Оценка пользователем {} центра {}".format(self.user, self.center)

    class Meta:
        verbose_name = "Оценка пользователя"
        verbose_name_plural = "Оценки пользователей"


class Tag(models.Model):
    name = models.CharField("Название", max_length=120)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Article(models.Model):
    name = models.TextField("Название")
    short_desc = models.TextField("Краткое описание")
    image = models.TextField("Изображение", blank=True, null=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Event(models.Model):
    name = models.TextField("Название")
    start_date = models.DateTimeField("Дата начала")
    place = models.TextField("Место проведения")
    contact_data = models.ForeignKey(
        ContactData, models.SET_NULL, related_name="events", null=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class EventRegistration(models.Model):
    user = models.ForeignKey(
        CustomUser, models.SET_NULL, null=True, related_name="events"
    )
    event = models.ForeignKey(Event, models.SET_NULL, null=True, related_name="users")

    def __str__(self) -> str:
        return "Регистрация пользователя {} на событие {}".format(self.user, self.event)

    class Meta:
        verbose_name = "Регистрация на событие"
        verbose_name_plural = "Регистрации на событие"


class SocialHelp(models.Model):
    name = models.TextField("Название")
    description = models.TextField("Описание")
    criteria = models.TextField("Критерии и оценки")
    support = models.TextField("Выгоды и поддержка")
    contact_data = models.ForeignKey(
        ContactData, models.SET_NULL, related_name="social_helps", null=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Социальная помощь"
        verbose_name_plural = "Социальная помощь"
