# Generated by Django 4.2.4 on 2023-08-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0023_book_num_pass_book_course_num_pass_course_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="bookQuiz",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="question", to="quizzes.bookquiz"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="courseQuiz",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="question", to="quizzes.coursequiz"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="levelQuiz",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="question", to="quizzes.levelquiz"
            ),
        ),
    ]