from django.contrib import admin
from .models import FeePayment

@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_fee', 'amount_paid', 'date_paid', 'reference_number')
    search_fields = ('student__adm_number', 'student__first_name', 'student__last_name', 'reference_number')
    list_filter = ('date_paid',)
    
    fields = ('student', 'total_fee', 'amount_paid', 'reference_number')