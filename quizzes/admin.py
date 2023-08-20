from django.contrib import admin


from .models import Answer, Book, Question, Quiz, Topic



# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = [
        'name',
	     'tag'

        ]
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = [
        'name',
	    'description',
        ]
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
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
    fields = [
        'question_text',
        'quiz',
        ]
    list_display = [
        'question_text',
        'quiz',
        'date_created',
        ]
    inlines = [
        AnswerInlineModel, 
        ] 