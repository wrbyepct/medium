# Generated by Django 5.0.6 on 2024-12-24 15:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("responses", "0004_alter_response_options_response_claps_count"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="response",
            options={"ordering": ["-claps_count"]},
        ),
    ]
