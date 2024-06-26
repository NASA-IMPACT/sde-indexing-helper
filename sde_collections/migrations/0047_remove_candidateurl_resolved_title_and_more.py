# Generated by Django 4.2.9 on 2024-05-21 21:18

from django.db import migrations, models
import sde_collections.models.pattern


class Migration(migrations.Migration):

    dependencies = [
        ("sde_collections", "0046_resolvedtitle_candidateurl_resolved_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidateurl",
            name="resolved_title",
        ),
        migrations.AlterField(
            model_name="titlepattern",
            name="title_pattern",
            field=models.CharField(
                help_text="This is the pattern for the new title. You can either write an exact replacement string (no quotes required) or you can write sinequa-valid code",
                validators=[sde_collections.models.pattern.validate_title_pattern],
                verbose_name="Title Pattern",
            ),
        ),
    ]
