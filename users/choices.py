from django.db import models


class GenderChoices(models.TextChoices):
    M = "MALE", "Мужской"
    F = "FEMALE", "Женский"
