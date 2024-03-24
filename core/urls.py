from django.urls import path
from .views import StudentDetailView, TopStudentsAPIView

urlpatterns = [
    path('student/', StudentDetailView.as_view(), name='student'),
    path('top-students/', TopStudentsAPIView.as_view(), name='top_students_api'),
]