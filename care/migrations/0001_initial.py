# Generated by Django 4.2.6 on 2023-10-14 14:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0003_contactdata_city"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ReabilatationCenter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(verbose_name="Название")),
                (
                    "description",
                    models.TextField(verbose_name="Описание предоставляемых услуг"),
                ),
                ("schedule", models.TextField(verbose_name="Расписание работы")),
                (
                    "specialisation",
                    models.CharField(
                        choices=[
                            ("MEDICAL", "Медицинская реабилитация"),
                            ("PHYSICAL", "Физическая реабилитация"),
                            ("PSYCHOLOGICAL", "Психологическая реабилитация"),
                            ("SOCIAL", "Социально-бытовая реабилитация"),
                            ("PROFESSIONAL", "Профессиональная реабилитация"),
                        ],
                        max_length=16,
                        verbose_name="Специализация",
                    ),
                ),
                (
                    "contact_data",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="centers",
                        to="users.contactdata",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CenterRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField(verbose_name="Оценка")),
                (
                    "date",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата оценки"),
                ),
                (
                    "center",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ratings",
                        to="care.reabilatationcenter",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ratings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
