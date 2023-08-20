from django.shortcuts import render

from quizzes.serializers import BookSerializer, QuestionSerializer, QuizSerializer, TopicSerializer
from .models import Question, Quiz, Topic, Book
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
# Create your views here.

class TopicApiModeView(ModelViewSet):

    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

class BookApiModeView(ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

class QuizzesApiView(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic', 'book']

class QuestionsrApiView(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz']