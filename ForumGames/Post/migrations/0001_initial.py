# Generated by Django 5.0 on 2023-12-07 17:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Videogame", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("P_ID_num", models.AutoField(primary_key=True, serialize=False)),
                ("Title", models.CharField(max_length=10)),
                ("Description", models.CharField(max_length=500)),
                ("FPS_ex", models.IntegerField()),
                (
                    "user_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "videogames_id",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="Videogame.possvideogames",
                    ),
                ),
            ],
        ),
    ]
