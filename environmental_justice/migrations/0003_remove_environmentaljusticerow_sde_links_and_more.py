# Generated by Django 5.0.1 on 2024-03-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("environmental_justice", "0002_environmentaljusticerow_sde_links"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="environmentaljusticerow",
            name="sde_links",
        ),
        migrations.AddField(
            model_name="environmentaljusticerow",
            name="sde_link",
            field=models.CharField(blank=True, default="", verbose_name="SDE Link"),
        ),
    ]