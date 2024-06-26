# Generated by Django 4.2.6 on 2023-12-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContentCurationRequest",
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
                ("name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("scientific_focus", models.CharField(max_length=200)),
                ("data_type", models.CharField(max_length=100)),
                ("data_link", models.CharField(max_length=1000)),
                ("additional_info", models.TextField()),
            ],
            options={
                "verbose_name": "Content Curation Request",
                "verbose_name_plural": "Content Curation Requests",
            },
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=400)),
                ("comments", models.TextField()),
            ],
            options={
                "verbose_name": "Feedback Response",
                "verbose_name_plural": "Feedback Responses",
            },
        ),
    ]
