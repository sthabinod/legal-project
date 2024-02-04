# Generated by Django 5.0 on 2024-02-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("case", "0004_casereportd"),
    ]

    operations = [
        migrations.AlterField(
            model_name="casereportd",
            name="status",
            field=models.CharField(
                choices=[("निष्क्रिय", "निष्क्रिय"), ("सक्रिय", "सक्रिय")],
                default="active",
                max_length=20,
            ),
        ),
    ]
