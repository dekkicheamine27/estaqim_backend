from .views import  MosabakaApiModeView,CreateMosabakaScoreView, CourseApiView, LevelApiModeView,  QuizzesApiView, QuestionsrApiView, BookApiModeView, TopicApiModeView, HadithApiModeView, QuizScoreApiView
from rest_framework import routers


router = routers.DefaultRouter()

router.register('topics', TopicApiModeView, basename='topics')
router.register('levels', LevelApiModeView, basename='levels')
router.register('books', BookApiModeView, basename='books')
router.register('courses', CourseApiView, basename='courses')
router.register('quizzes', QuizzesApiView, basename='quizzes')
router.register('questions', QuestionsrApiView, basename='questions')
router.register('hadiths', HadithApiModeView, basename='hadiths')
router.register('mosabakat', MosabakaApiModeView, basename='mosabaka')
router.register('quizScore', QuizScoreApiView, basename='quizScore')
router.register('mosabakascore', CreateMosabakaScoreView, basename='mosabakascore')

urlpatterns =  router.urls

