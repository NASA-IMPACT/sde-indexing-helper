# Generated by Django 4.2.6 on 2023-11-26 17:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sde_collections", "0036_candidateurl_present_on_prod_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="collection",
            name="has_sinequa_config",
        ),
    ]
