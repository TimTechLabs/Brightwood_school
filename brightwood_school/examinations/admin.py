from django.contrib import admin
from .models import StudentReport

@admin.register(StudentReport)
class StudentReportAdmin(admin.ModelAdmin):
    list_display = (
        'student', 'term', 'mean_score', 'mean_grade',
        'maths', 'maths_grade',
        'english', 'english_grade',
        'kiswahili', 'kiswahili_grade',
        'chemistry', 'chemistry_grade',
        'biology', 'biology_grade'
    )
    search_fields = ('student__adm_number', 'student__first_name', 'student__last_name')
    list_filter = ('term',)
    
    fieldsets = (
        ('Student & Term Information', {
            'fields': ('student', 'term')
        }),
        ('Subject Marks (Enter 0-100)', {
            'fields': ('maths', 'english', 'kiswahili', 'chemistry', 'biology')
        }),
        ('Calculated Performance (Auto)', {
            'fields': ('mean_score', 'mean_grade', 'maths_grade', 'english_grade', 'kiswahili_grade', 'chemistry_grade', 'biology_grade'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('mean_score', 'mean_grade', 'maths_grade', 'english_grade', 'kiswahili_grade', 'chemistry_grade', 'biology_grade')