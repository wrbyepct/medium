# Generated by Django 5.0.6 on 2024-12-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_clap_clap_unique_article_per_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="responses_count",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
