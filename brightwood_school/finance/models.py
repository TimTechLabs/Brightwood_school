from django.db import models
from django.utils import timezone
from students.models import StudentProfile

class FeePayment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='fee_payments')
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, default=50000.00)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_paid = models.DateField(default=timezone.now)
    reference_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.student.admission_number} - KES {self.amount_paid}"