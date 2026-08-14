# examinations/admin.py
from django.contrib import admin
from .models import Exam, Mark

admin.site.register(Exam)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'subject', 'score', 'out_of')
    list_filter = ('exam', 'subject')
    search_fields = ('student__admission_number', 'student__user__username')