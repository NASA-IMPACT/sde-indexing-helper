# Generated by Django 4.2.9 on 2024-05-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sde_collections", "0049_alter_resolvedtitle_resolution_date_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resolvedtitle",
            name="resolved_title",
            field=models.CharField(blank=True),
        ),
    ]
