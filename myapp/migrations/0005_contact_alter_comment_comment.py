# Generated by Django 4.1.5 on 2023-02-23 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_comment_comment_alter_comment_website"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("is_resolved", models.BooleanField(default=False)),
                ("contacted_date", models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
        migrations.AlterField(
            model_name="comment",
            name="comment",
            field=models.TextField(),
        ),
    ]
