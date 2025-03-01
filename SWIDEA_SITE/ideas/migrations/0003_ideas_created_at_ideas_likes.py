# Generated by Django 5.1.5 on 2025-01-15 23:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ideas", "0002_alter_ideas_photo_alter_ideas_tool"),
    ]

    operations = [
        migrations.AddField(
            model_name="ideas",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ideas",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]
