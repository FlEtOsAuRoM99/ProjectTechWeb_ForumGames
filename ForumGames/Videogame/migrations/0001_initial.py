# Generated by Django 5.0 on 2023-12-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PossVideogames",
            fields=[
                (
                    "name",
                    models.CharField(max_length=25, primary_key=True, serialize=False),
                ),
                ("Description", models.CharField(max_length=500)),
            ],
        ),
    ]
