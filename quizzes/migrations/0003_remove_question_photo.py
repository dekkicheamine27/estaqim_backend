# Generated by Django 4.1.3 on 2023-08-18 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_book_quiz_topic_quiz_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='photo',
        ),
    ]
