from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from users.choices import GenderChoices

from .managers import CustomUserManager


class ContactData(models.Model):
    phone = models.TextField("Номер телефона", blank=True)
    city = models.TextField("Город", blank=True)
    address = models.TextField("Адрес", blank=True)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("Электронная почта", unique=True)
    last_name = models.TextField("Фамилия пользователя", default="")
    first_name = models.TextField("Имя пользователя", default="")
    middle_name = models.TextField("Отчество пользователя", default="")
    date_of_birth = models.DateField("Дата рождения пользователя", default=timezone.now)
    gender = models.CharField(
        "Пол пользователя", max_length=6, choices=GenderChoices.choices, null=True
    )
    contact_data = models.ForeignKey(
        ContactData, models.SET_NULL, related_name="users", null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
