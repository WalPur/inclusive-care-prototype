# Generated by Django 4.2.6 on 2023-10-16 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_contactdata_options_alter_customuser_options"),
        ("care", "0004_event_eventregistration"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={"verbose_name": "Событие", "verbose_name_plural": "События"},
        ),
        migrations.AlterModelOptions(
            name="eventregistration",
            options={
                "verbose_name": "Регистрация на событие",
                "verbose_name_plural": "Регистрации на событие",
            },
        ),
        migrations.CreateModel(
            name="SocialHelp",
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
                ("description", models.TextField(verbose_name="Описание")),
                ("criteria", models.TextField(verbose_name="Критерии и оценки")),
                ("support", models.TextField(verbose_name="Выгоды и поддержка")),
                (
                    "contact_data",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="social_helps",
                        to="users.contactdata",
                    ),
                ),
            ],
            options={
                "verbose_name": "Социальная помощь",
                "verbose_name_plural": "Социальная помощь",
            },
        ),
    ]