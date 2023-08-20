
from rest_framework import serializers
from .models import Answer, Book, Question, Quiz, Topic

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = [
            'id',
            'name',
            'tag'
            
        ]

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'description',
            'image'
            
        ]

class QuizSerializer(serializers.ModelSerializer):
    num_questions = serializers.ReadOnlyField()
    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'num_questions'
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'answer_text',
            'is_right',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)


    class Meta:
    
        model = Question
        fields = [
            'question_text', 'answer',
        ]