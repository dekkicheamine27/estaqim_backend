# Generated by Django 4.2.4 on 2024-03-16 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0045_mosabaka_book_pdf_mosabaka_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mosabaka",
            old_name="is_active",
            new_name="active",
        ),
    ]