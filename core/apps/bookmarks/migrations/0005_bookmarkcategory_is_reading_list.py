# Generated by Django 5.0.6 on 2024-12-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookmarks", "0004_bookmarkcategory_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmarkcategory",
            name="is_reading_list",
            field=models.BooleanField(default=True),
        ),
    ]
