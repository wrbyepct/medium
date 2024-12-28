# Generated by Django 5.0.6 on 2024-12-25 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("responses", "0005_alter_response_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="response",
            name="level",
        ),
        migrations.RemoveField(
            model_name="response",
            name="lft",
        ),
        migrations.RemoveField(
            model_name="response",
            name="rght",
        ),
        migrations.RemoveField(
            model_name="response",
            name="tree_id",
        ),
        migrations.AlterField(
            model_name="response",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="responses.response",
            ),
        ),
    ]
