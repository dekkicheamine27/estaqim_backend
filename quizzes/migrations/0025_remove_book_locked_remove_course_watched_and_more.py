# Generated by Django 4.2.4 on 2023-08-29 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0024_alter_question_bookquiz_alter_question_coursequiz_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="locked",
        ),
        migrations.RemoveField(
            model_name="course",
            name="watched",
        ),
        migrations.RemoveField(
            model_name="level",
            name="locked",
        ),
    ]