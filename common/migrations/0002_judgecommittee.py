# Generated by Django 5.0 on 2024-01-01 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JudgeCommittee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="judge_committee")),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=20,
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "designation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.designation",
                    ),
                ),
            ],
        ),
    ]
