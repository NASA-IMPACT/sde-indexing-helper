# Generated by Django 5.0.1 on 2024-02-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sde_collections", "0040_candidateurl_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidateurl",
            name="hash",
            field=models.CharField(
                blank=True, default="1", max_length=32, verbose_name="Hash"
            ),
        ),
    ]