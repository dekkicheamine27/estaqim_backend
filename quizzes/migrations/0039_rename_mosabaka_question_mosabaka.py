# Generated by Django 4.2.4 on 2024-03-03 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0038_alter_mosabakascore_mosabaka"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="Mosabaka",
            new_name="mosabaka",
        ),
    ]