# Generated by Django 5.0 on 2024-02-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("act_law", "0004_courttype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actlaw",
            name="status",
            field=models.CharField(
                choices=[("निष्क्रिय", "निष्क्रिय"), ("सक्रिय", "सक्रिय")],
                default="सक्रिय",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="courttype",
            name="status",
            field=models.CharField(
                choices=[("निष्क्रिय", "निष्क्रिय"), ("सक्रिय", "सक्रिय")],
                default="सक्रिय",
                max_length=20,
            ),
        ),
    ]
