from django.contrib import admin


from .models import Answer, Book, Course, Hadith, Level, CourseQuiz, BookQuiz, LevelQuiz ,Question, Quiz, Topic, Mosabaka, MosabakaScore



# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = [
        'name',
	'tag'

        ]

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	list_display = [
        'name',
	'num_pass_level',

        ]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_filter = ["level"]
	list_display = [
        'name',
	'book_order',
	'description',
	'num_pass_book',
	'is_active'
        ]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_filter = ["book"]
	list_display = [
        'name',
	'video_url',
	'course_order',
	'num_pass_course',
        ]


@admin.register(LevelQuiz)
class LevelQuizAdmin(admin.ModelAdmin):


	list_display = [
        'title',
        ]


@admin.register(BookQuiz)
class BookQuizAdmin(admin.ModelAdmin):


	list_display = [
        'title',
        ]

@admin.register(CourseQuiz)
class CourseQuizAdmin(admin.ModelAdmin):


	list_display = [
        'title',
        ]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
	list_display = [

        'title',
        ]


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right'
        ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ["levelQuiz", "bookQuiz", "courseQuiz", "quiz", "mosabaka"]
    fields = [
        'question_text',
        'quiz',
        "mosabaka",
	'levelQuiz',
        'bookQuiz',
        'courseQuiz'

        ]
    list_display = [
        'question_text',
        'quiz',
        'date_created',
        ]
    inlines = [
        AnswerInlineModel,
        ]

@admin.register(Hadith)
class HadithAdmin(admin.ModelAdmin):
	list_display = [
        'id',
        'title',
	     'body',
	     'rawi',
        ]


@admin.register(Mosabaka)
class MosabakaAdmin(admin.ModelAdmin):
	list_display = [

        'title',
	     'mosabaka_order',
	     'active'
        ]

@admin.register(MosabakaScore)
class MosabakaScoreAdmin(admin.ModelAdmin):
	list_display = [

        'student',
	     'mosabaka',
	     'score'
        ]