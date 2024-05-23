# Generated by Django 4.2.9 on 2024-05-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sde_collections", "0054_resolvedtitle_active_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="titlepattern",
            name="matched_urls",
            field=models.ManyToManyField(
                related_name="title_patterns",
                through="sde_collections.ResolvedTitle",
                to="sde_collections.candidateurl",
            ),
        ),
    ]
