# Generated by Django 5.1.5 on 2025-01-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="photo",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
