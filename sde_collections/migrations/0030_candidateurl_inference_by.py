# Generated by Django 4.2.3 on 2023-09-01 05:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sde_collections", "0029_alter_candidateurl_document_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidateurl",
            name="inferenced_by",
            field=models.CharField(
                blank=True,
                default="",
                help_text="This keeps track of who inferenced document type",
                verbose_name="Inferenced By",
            ),
        ),
    ]
