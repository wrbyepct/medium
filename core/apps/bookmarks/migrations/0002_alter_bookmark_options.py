# Generated by Django 5.0.6 on 2024-12-19 14:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookmarks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookmark",
            options={"ordering": ["-created_at"]},
        ),
    ]
