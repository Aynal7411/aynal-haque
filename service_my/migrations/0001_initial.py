# Generated by Django 5.2.1 on 2025-05-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "icon",
                    models.CharField(
                        help_text="Use Bootstrap icons, e.g., 'bi-code', 'bi-brush'",
                        max_length=50,
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ["order"],
            },
        ),
    ]
