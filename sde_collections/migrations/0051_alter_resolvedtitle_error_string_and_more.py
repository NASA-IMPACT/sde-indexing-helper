# Generated by Django 4.2.9 on 2024-05-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sde_collections", "0050_alter_resolvedtitle_resolved_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resolvedtitle",
            name="error_string",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="resolvedtitle",
            name="resolved_title",
            field=models.CharField(blank=True, default=""),
        ),
    ]