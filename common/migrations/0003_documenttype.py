# Generated by Django 5.0 on 2024-01-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_judgecommittee"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentType",
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
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=20,
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
    ]
