# finance/admin.py
from django.contrib import admin
from .models import FeePayment

@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_fees', 'amount_paid', 'balance', 'status', 'last_payment_date')
    list_filter = ('status', 'last_payment_date')
    search_fields = ('student__admission_number', 'student__user__username')