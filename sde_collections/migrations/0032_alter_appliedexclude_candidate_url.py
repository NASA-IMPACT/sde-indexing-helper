# Generated by Django 4.2 on 2023-04-27 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sde_collections", "0031_candidateurl_excludes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appliedexclude",
            name="candidate_url",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="sde_collections.candidateurl",
            ),
        ),
    ]
