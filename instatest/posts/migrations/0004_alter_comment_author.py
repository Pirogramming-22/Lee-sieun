# Generated by Django 5.1.5 on 2025-01-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.CharField(max_length=50),
        ),
    ]
