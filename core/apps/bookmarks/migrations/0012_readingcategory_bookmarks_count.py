# Generated by Django 5.0.6 on 2024-12-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookmarks", "0011_alter_readingcategory_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="readingcategory",
            name="bookmarks_count",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
