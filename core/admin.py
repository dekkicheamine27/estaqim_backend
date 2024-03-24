from django.contrib import admin
from .models import Student



class StudentAdmin(admin.ModelAdmin):
  list_display = (  'name', 'email', 'level', 'book', 'course', 'country', 'city', 'score','date_created')
  search_fields = ['name', 'city']

admin.site.register(Student, StudentAdmin)