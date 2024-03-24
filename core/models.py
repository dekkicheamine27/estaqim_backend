from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Student(models.Model):
    firebase_uid = models.CharField(max_length=128, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    city = models.CharField(max_length=255, default="الجزائر")
    country = models.CharField(max_length=255, default="الجزائر")# Added city field
    birthday = models.DateField(default=datetime.date(2000, 1, 1))
    level = models.PositiveIntegerField(default=1)
    book = models.PositiveIntegerField(default=1)
    course = models.PositiveIntegerField(default=1)
    mosabaka = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['score']




    def __str__(self) -> str:
        return f'{self.name}'