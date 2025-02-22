# Generated by Django 5.0.6 on 2024-12-06 17:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="articleview",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="articleview",
            constraint=models.UniqueConstraint(
                fields=("user", "article", "viewer_ip"),
                name="unqiue_view_per_article_user_ip",
            ),
        ),
    ]
