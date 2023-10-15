# Generated by Django 4.2.6 on 2023-10-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("care", "0002_centerrating_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=120, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.AlterModelOptions(
            name="centerrating",
            options={
                "verbose_name": "Оценка пользователя",
                "verbose_name_plural": "Оценки пользователей",
            },
        ),
        migrations.AlterModelOptions(
            name="reabilatationcenter",
            options={
                "verbose_name": "Реабилитационный центр",
                "verbose_name_plural": "Реабилитационные центры",
            },
        ),
        migrations.CreateModel(
            name="Article",
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
                ("short_desc", models.TextField(verbose_name="Краткое описание")),
                (
                    "image",
                    models.TextField(blank=True, null=True, verbose_name="Изображение"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                ("tags", models.ManyToManyField(null=True, to="care.tag")),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
    ]
