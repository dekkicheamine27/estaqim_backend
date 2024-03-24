from django.db import models
from radio_estaqim import settings

# Create your models here.

class Topic(models.Model):
    class Meta:
        verbose_name = ("Topic")
        verbose_name_plural = ("Topics")
        ordering = ['id']
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Level(models.Model):
    class Meta:
        verbose_name = ("Level")
        verbose_name_plural = ("Levels")
        ordering = ['id']
    name = models.CharField(max_length=255)
    level_order = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='levels', blank=True)
    level_pdf = models.FileField(upload_to='pdfs/level/', null=True , blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, null=True, blank=True)
    num_pass_level = models.PositiveIntegerField(default=0)
    is_last = models.BooleanField(default=False)

    def num_books(self):
        return self.book.count()

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")
        ordering = ['book_order']
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    book_order = models.IntegerField(null=True, blank=True)
    book_pdf = models.FileField(upload_to='pdfs/book/', null=True , blank=True)
    level = models.ForeignKey(Level,related_name="book" , on_delete=models.DO_NOTHING, null=True, blank=True)
    image = models.ImageField(upload_to='books', blank=True)
    num_pass_book= models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False, verbose_name=("Active Status"))
    is_last = models.BooleanField(default=False)


    def num_courses(self):
        return self.course.count()

    def __str__(self):
        return self.name

class Course(models.Model):
    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")
        ordering = ['id']
    name = models.CharField(max_length=255)
    course_order = models.IntegerField(null=True, blank=True)
    video_url = models.URLField()
    num_pass_course = models.PositiveIntegerField(default=0)
    book = models.ForeignKey(Book,related_name="course" , on_delete=models.DO_NOTHING, null=True, blank=True)
    is_last = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class LevelQuiz(models.Model):

    class Meta:
        verbose_name = ("LevelQuiz")
        verbose_name_plural = ("LevelsQuizzes")
        ordering = ['id']


    title = models.CharField(max_length=255,  verbose_name=("Quiz Title"))
    level = models.OneToOneField(Level, related_name="quiz" ,on_delete=models.DO_NOTHING, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def num_questions(self):
        return self.question.count()

    def __str__(self):
        return self.title



class BookQuiz(models.Model):

    class Meta:
        verbose_name = ("BookQuiz")
        verbose_name_plural = ("BooksQuizzes")
        ordering = ['id']


    title = models.CharField(max_length=255,  verbose_name=("Quiz Title"))
    book = models.OneToOneField(Book, related_name="quiz" ,on_delete=models.DO_NOTHING, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def num_questions(self):
        return self.question.count()

    def __str__(self):
        return self.title



class CourseQuiz(models.Model):

    class Meta:
        verbose_name = ("CourseQuiz")
        verbose_name_plural = ("CoursesQuizzes")
        ordering = ['id']


    title = models.CharField(max_length=255,  verbose_name=("Quiz Title"))
    course = models.OneToOneField(Course, related_name="quiz" ,on_delete=models.DO_NOTHING, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def num_questions(self):
        return self.question.count()

    def __str__(self):
        return self.title






class Quiz(models.Model):

    class Meta:
        verbose_name = ("quiz")
        verbose_name_plural = ("Quizzes")
        ordering = ['id']


    title = models.CharField(max_length=255, default=(
        "New Quiz"), verbose_name=("Quiz Title"))
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, null=True, blank=True)

    # Foreign Key to Book
    to_save = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def num_questions(self):
        return self.question.count()

    def __str__(self):
        return self.title


class Mosabaka(models.Model):

    class Meta:
        verbose_name = ("Mosabaka")
        verbose_name_plural = ("Mosabakat")
        ordering = ['id']


    title = models.CharField(max_length=255,  verbose_name=("Mosabka Title"))
    description = models.TextField(default="")
    mosabaka_order = models.IntegerField(null=True, blank=True)
    book_pdf = models.FileField(upload_to='pdfs/mosabakat/', null=True , blank=True)
    active = models.BooleanField(
        default=False, verbose_name=("Active Status"))
    is_ready = models.BooleanField(default=False,)


    def __str__(self):
        return self.title


class Question(models.Model):

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")
        ordering = ['id']

    question_text = models.CharField(max_length=255, verbose_name=("Title"))
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE, blank=True, null=True)
    mosabaka = models.ManyToManyField(Mosabaka, related_name='question', blank=True)
    courseQuiz = models.ManyToManyField(CourseQuiz, related_name='question', blank=True)
    bookQuiz = models.ManyToManyField(BookQuiz, related_name='question', blank=True)
    levelQuiz = models.ManyToManyField(LevelQuiz, related_name='question', blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=("Active Status"))



    def __str__(self):
        return self.question_text


class Answer(models.Model):
    class Meta:
        verbose_name = ("Answer")
        verbose_name_plural = ("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(
        max_length=255, verbose_name=("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Hadith(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    rawi = models.CharField(max_length=255)

    def __str__(self):
        return self.body

class Candidate(models.Model):
    class Meta:
        verbose_name = ("Condidate")
        verbose_name_plural = ("Condidates")
        ordering = ['-score']
    name = models.CharField(max_length=255)
    score = models.IntegerField()

    def __str__(self):
        return self.name


class QuizScore(models.Model):
    QUIZ_TYPES = (
        ('book', 'Book'),
        ('course', 'Course'),
        ('level', 'Level')
    )

    quiz_type = models.CharField(max_length=10, choices=QUIZ_TYPES, default='course')
    student = models.ForeignKey(settings.STUDENT_MODEL, on_delete=models.CASCADE)
    quiz_level = models.ForeignKey(LevelQuiz, on_delete=models.CASCADE, null=True, blank=True)
    quiz_book = models.ForeignKey(BookQuiz, on_delete=models.CASCADE, null=True, blank=True)
    quiz_course= models.ForeignKey(CourseQuiz, on_delete=models.CASCADE, null=True, blank=True)
    score = models.PositiveIntegerField(default=0)

class MosabakaScore(models.Model):
    student = models.ForeignKey(settings.STUDENT_MODEL, on_delete=models.CASCADE)
    mosabaka = models.ForeignKey(Mosabaka, blank=True, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)