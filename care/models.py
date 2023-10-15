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
