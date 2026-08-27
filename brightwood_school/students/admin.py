from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('admission_number', 'current_class', 'user')
    fields = ('user', 'admission_number', 'current_class')