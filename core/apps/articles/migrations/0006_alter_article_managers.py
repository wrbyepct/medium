# Generated by Django 5.0.6 on 2025-01-01 15:24

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0005_remove_article_responses_count"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="article",
            managers=[
                ("statistic_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
