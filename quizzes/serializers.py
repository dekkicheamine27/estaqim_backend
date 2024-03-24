
from rest_framework import serializers
from .models import Answer, Book, Mosabaka, MosabakaScore, Course, Hadith, Level, CourseQuiz, BookQuiz, LevelQuiz, Question, Quiz, QuizScore, Topic


class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = [
            'id',
            'name',
            'tag',
            'active'
            
        ]

class LevelQuizSerializer(serializers.ModelSerializer):
    num_questions = serializers.ReadOnlyField()
    class Meta:
        model = LevelQuiz
        fields = [
            'id',
            'title',
            'num_questions',
        ]


class BookQuizSerializer(serializers.ModelSerializer):
    num_questions = serializers.ReadOnlyField()
    class Meta:
        model = BookQuiz
        fields = [
            'id',
            'title',
            'num_questions'
        ]

class CourseQuizSerializer(serializers.ModelSerializer):
    num_questions = serializers.ReadOnlyField()
    class Meta:
        model = CourseQuiz
        fields = [
            'id',
            'title',
            'num_questions'
        ]

class LevelSerializer(serializers.ModelSerializer):
    quiz = LevelQuizSerializer(read_only=True)
    num_books = serializers.ReadOnlyField()
    class Meta:
        model = Level
        fields = [
            'id',
            'name',
            'level_order',
            'image',
            'level_pdf',
            'num_books',
            'num_pass_level',
            'quiz',
            'is_last' 
        ]

class BookSerializer(serializers.ModelSerializer):
    quiz = BookQuizSerializer()
    num_courses = serializers.ReadOnlyField()
    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'description',
            'book_order',
            "book_pdf",
            'image',
            'quiz'   ,
            'num_pass_book',
            'num_courses',
            'is_active',
            'is_last' 
             
        ]

class CourseSerializer(serializers.ModelSerializer):
    quiz = CourseQuizSerializer()
    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'course_order',
            'video_url',
            'num_pass_course',
            'quiz',
            'is_last' 
        ]





class QuizSerializer(serializers.ModelSerializer):
    num_questions = serializers.ReadOnlyField()
    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'to_save',
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


class HadithSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Hadith
        fields = [
           
        'title',
	     'body',
	     'rawi',
        ]



class QuizScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizScore
        fields = [
            'id','student', 'quiz_level', 'quiz_book', 'quiz_course', 'quiz_type', 'score',
        ]
    
class MosabakaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mosabaka
        fields = [
            'id',
         'title',
         'description',
	     'mosabaka_order',
         'book_pdf',
	     'active',
         'is_ready',
         
        ]

class MosabakaScoreSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    mosabaka_name = serializers.SerializerMethodField()
    class Meta:
        model = MosabakaScore
        fields = ['student', 'mosabaka', 'score', 'student_name', 'mosabaka_name']

    def get_student_name(self, obj):
        return obj.student.name 

    def get_mosabaka_name(self, obj):
        return obj.mosabaka.title