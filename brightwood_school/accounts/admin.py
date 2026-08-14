from django.contrib import admin
from .models import Student

# Hide all other models/apps from the admin index so ONLY Students remain
original_get_app_list = admin.site.get_app_list

def clean_admin_app_list(request, app_label=None):
    app_list = original_get_app_list(request, app_label)
    filtered_app_list = []
    for app in app_list:
        filtered_models = [m for m in app['models'] if m['object_name'].lower() == 'student']
        if filtered_models:
            app['models'] = filtered_models
            filtered_app_list.append(app)
    return filtered_app_list

admin.site.get_app_list = clean_admin_app_list

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('adm_number', 'first_name', 'last_name', 't1_mean', 't2_mean', 't3_mean', 'fees_balance')
    search_fields = ('adm_number', 'first_name', 'last_name')
    fieldsets = (
        ('Student Personal Information', {
            'fields': ('adm_number', 'first_name', 'last_name')
        }),
        ('Term 1 Performance (Math, Eng, Kis, History, CRE, Chem, Bio)', {
            'fields': ('t1_math', 't1_eng', 't1_kis', 't1_history', 't1_cre', 't1_chem', 't1_bio', 't1_mean')
        }),
        ('Term 2 Performance (Math, Eng, Kis, History, CRE, Chem, Bio)', {
            'fields': ('t2_math', 't2_eng', 't2_kis', 't2_history', 't2_cre', 't2_chem', 't2_bio', 't2_mean')
        }),
        ('Term 3 Performance (Math, Eng, Kis, History, CRE, Chem, Bio)', {
            'fields': ('t3_math', 't3_eng', 't3_kis', 't3_history', 't3_cre', 't3_chem', 't3_bio', 't3_mean')
        }),
        ('School Fees Status', {
            'fields': ('fees_paid', 'fees_balance')
        }),
    )