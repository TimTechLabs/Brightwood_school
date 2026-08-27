from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Adjust these tuple values to match actual fields on your Teacher model
    list_display = ('first_name', 'last_name')  
    search_fields = ('first_name', 'last_name')