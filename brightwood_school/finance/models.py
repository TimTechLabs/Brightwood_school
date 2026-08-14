# finance/models.py
from django.db import models
from students.models import Student

class FeePayment(models.Model):
    STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Partial', 'Partial'),
        ('Unpaid', 'Unpaid'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fee_payments')
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unpaid')
    last_payment_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically calculate balance before saving
        self.balance = self.total_fees - self.amount_paid
        if self.balance <= 0:
            self.status = 'Paid'
            self.balance = 0.00
        elif self.amount_paid > 0:
            self.status = 'Partial'
        else:
            self.status = 'Unpaid'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.admission_number} - Balance: {self.balance} ({self.status})"