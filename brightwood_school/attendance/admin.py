# attendance/admin.py
from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'classroom', 'date', 'status', 'marked_by')
    list_filter = ('date', 'status', 'classroom')
    search_fields = ('student__admission_number', 'student__user__username')