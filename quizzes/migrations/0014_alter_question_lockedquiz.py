# Generated by Django 4.2.4 on 2023-08-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0013_alter_question_lockedquiz"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="lockedQuiz",
            field=models.ManyToManyField(
                blank=True, related_name="question", to="quizzes.lockedquiz"
            ),
        ),
    ]