from quizzes.serializers import BookSerializer,  CourseSerializer, HadithSerializer,MosabakaSerializer, MosabakaScoreSerializer, LevelSerializer, QuestionSerializer, QuizSerializer, TopicSerializer, QuizScoreSerializer
from .models import  Course, Hadith, Level, Question, Quiz, Topic, Book, QuizScore, Mosabaka, MosabakaScore
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class HadithApiModeView(ModelViewSet):

    serializer_class = HadithSerializer
    queryset = Hadith.objects.all()

    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60*15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class TopicApiModeView(GenericViewSet, RetrieveModelMixin, ListModelMixin):

    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60*15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class LevelApiModeView(ModelViewSet):

    serializer_class = LevelSerializer
    queryset = Level.objects.all()

    @action(detail=True, methods=['post'])
    def increment_pass(self, request, pk=None):
        level = self.get_object()
        level.num_pass_level += 1
        level.save()
        return Response(status=status.HTTP_200_OK)

class BookApiModeView(ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['level']

    @action(detail=True, methods=['post'])
    def increment_pass(self, request, pk=None):
        level = self.get_object()
        level.num_pass_book += 1
        level.save()
        return Response(status=status.HTTP_200_OK)



    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

    def get_cache_key(self, request):
        key = super().get_cache_key(request)
        return key + '_' + ('_'.join(sorted(request.GET.keys())))


class CourseApiView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book']

    @action(detail=True, methods=['post'])
    def increment_pass(self, request, pk=None):
        level = self.get_object()
        level.num_pass_course += 1
        level.save()
        return Response(status=status.HTTP_200_OK)



    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

    def get_cache_key(self, request):
        key = super().get_cache_key(request)
        return key + '_' + ('_'.join(sorted(request.GET.keys())))






class QuizzesApiView(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic']



    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

    def get_cache_key(self, request):
        key = super().get_cache_key(request)
        return key + '_' + ('_'.join(sorted(request.GET.keys())))

class QuestionsrApiView(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz', 'levelQuiz', 'bookQuiz', 'courseQuiz', 'mosabaka']

    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

    def get_cache_key(self, request):
        key = super().get_cache_key(request)
        return key + '_' + ('_'.join(sorted(request.GET.keys())))


class MosabakaApiModeView(ModelViewSet):

    serializer_class = MosabakaSerializer
    queryset = Mosabaka.objects.all()

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

    def get_cache_key(self, request):
        key = super().get_cache_key(request)
        return key + '_' + ('_'.join(sorted(request.GET.keys())))

class CreateMosabakaScoreView(ModelViewSet):
    queryset = MosabakaScore.objects.all()
    serializer_class = MosabakaScoreSerializer

    def create(self, request, *args, **kwargs):
        student = request.data.get('student')
        mosabaka = request.data.get('mosabaka')
        score = request.data.get('score')

        # Check if a MosabakaScore instance already exists for the given student and mosabaka
        existing_instance = MosabakaScore.objects.filter(student=student, mosabaka=mosabaka).first()

        if existing_instance:
            # Update the existing instance with the new score

            serializer = self.get_serializer(existing_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Create a new instance
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizScoreApiView(ModelViewSet):
    queryset = QuizScore.objects.all()
    serializer_class = QuizScoreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student','quiz_level', 'quiz_book', 'quiz_course', 'quiz_type']

    @action(detail=False, methods=['get'], url_path='get-or-create')
    def get_or_create_quiz_score(self, request):
        student_id = int(request.query_params.get('student_id'))
        quiz_id = int(request.query_params.get('quiz_id'))
        quiz_type = request.query_params.get('quiz_type')

        # Logic to determine the quiz_fk_field based on quiz_type remains the same
        quiz_fk_field = {
            'book': 'quiz_book_id',
            'course': 'quiz_course_id',
            'level': 'quiz_level_id'
        }.get(quiz_type, 'quiz_course_id')

        filter_kwargs = {
            'student_id': student_id,
            'quiz_type': quiz_type,
            # Assuming quiz_fk_field is determined based on quiz_type
            quiz_fk_field: quiz_id
        }

        quiz_score, created = QuizScore.objects.get_or_create(
            defaults={'score': request.query_params.get('score', 0)},  # Providing a default score
            **filter_kwargs
        )

        serializer = self.get_serializer(quiz_score)
        return Response(serializer.data, status=status.HTTP_200_OK )

    def create(self, request, *args, **kwargs):
        quiz_type = request.data.get('quiz_type')
        student_id = request.data.get('student')
        # Assuming 'quiz_id' is passed to identify the specific quiz (level/book/course)
        quiz_id = request.data.get('quiz_id')

        # Find the specific quiz foreign key field based on quiz_type
        quiz_fk_field = {
            'book': 'quiz_book_id',
            'course': 'quiz_course_id',
            'level': 'quiz_level_id'
        }.get(quiz_type, 'quiz_course_id')  # Default to 'quiz_course_id' if not found

        filter_kwargs = {
            'quiz_type': quiz_type,
            'student_id': student_id,
            quiz_fk_field: quiz_id
        }

        quiz_score, created = QuizScore.objects.update_or_create(
            defaults={'score': request.data.get('score')},
            **filter_kwargs
        )

        serializer = self.get_serializer(quiz_score)
        return Response(serializer.data)

