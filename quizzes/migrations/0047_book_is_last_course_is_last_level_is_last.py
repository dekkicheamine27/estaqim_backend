# Generated by Django 4.2.4 on 2024-03-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0046_rename_is_active_mosabaka_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_last",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="course",
            name="is_last",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="level",
            name="is_last",
            field=models.BooleanField(default=False),
        ),
    ]