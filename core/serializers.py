

from rest_framework import serializers
from .models import Student






class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','email','city', 'country', 'birthday', 'level', 'book', 'course', 'mosabaka', 'score']

class StudentOrderSerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = [ 'rank', 'name','level', 'book', 'course', 'score']
