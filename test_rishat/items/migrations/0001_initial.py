# Generated by Django 4.1.1 on 2022-09-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=150, verbose_name="Название")),
                (
                    "description",
                    models.TextField(max_length=1000, verbose_name="Описание"),
                ),
                ("price", models.IntegerField(verbose_name="Цена")),
            ],
        ),
    ]
