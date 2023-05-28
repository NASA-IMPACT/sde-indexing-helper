# Generated by Django 4.2 on 2023-05-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "sde_collections",
            "0010_rename_pattern_type_titlepattern_match_pattern_type_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="titlepattern",
            name="title_pattern_type",
            field=models.IntegerField(
                choices=[(1, "Plain Text"), (2, "Modifier"), (3, "Xpath")], default=1
            ),
        ),
    ]