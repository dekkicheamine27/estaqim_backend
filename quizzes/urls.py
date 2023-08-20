from django.urls import path, include
from .views import  QuizzesApiView, QuestionsrApiView, BookApiModeView, TopicApiModeView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('topics', TopicApiModeView, basename='topics')
router.register('books', BookApiModeView, basename='books')
router.register('quizzes', QuizzesApiView, basename='quizzes')
router.register('questions', QuestionsrApiView, basename='questions')


urlpatterns =  router.urls
