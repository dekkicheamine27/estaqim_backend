from django.db import models

# Create your models here.

class Topic(models.Model):
    class Meta:
        verbose_name = ("Topic")
        verbose_name_plural = ("Topics")
        ordering = ['id']
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name



class Book(models.Model):
    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")
        ordering = ['id']
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to='books', blank=True)


    def __str__(self):
        return self.name



class Quiz(models.Model):

    class Meta:
        verbose_name_plural = ("Quizzes")
        ordering = ['id']


    title = models.CharField(max_length=255, default=(
        "New Quiz"), verbose_name=("Quiz Title"))
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    
    # Foreign Key to Book
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)

    def num_questions(self):
        return self.question.count()

    def __str__(self):
        return self.title

class Question(models.Model):

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")
        ordering = ['id']
    
    question_text = models.CharField(max_length=255, verbose_name=("Title"))
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE)
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