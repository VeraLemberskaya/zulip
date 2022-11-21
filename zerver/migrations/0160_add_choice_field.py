# Generated by Django 1.11.11 on 2018-04-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0159_realm_google_hangouts_domain"),
    ]

    operations = [
        migrations.AddField(
            model_name="customprofilefield",
            name="field_data",
            field=models.TextField(default="", null=True),
        ),
        migrations.AlterField(
            model_name="customprofilefield",
            name="field_type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Short text"), (2, "Long text"), (3, "Choice")], default=1
            ),
        ),
    ]
