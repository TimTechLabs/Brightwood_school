from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Student(models.Model):
    adm_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    # Term 1 Subjects & Mean
    t1_math = models.CharField(max_length=10, default='B+')
    t1_eng = models.CharField(max_length=10, default='A-')
    t1_kis = models.CharField(max_length=10, default='B')
    t1_history = models.CharField(max_length=10, default='B+')
    t1_cre = models.CharField(max_length=10, default='A-')
    t1_chem = models.CharField(max_length=10, default='B+')
    t1_bio = models.CharField(max_length=10, default='A-')
    t1_mean = models.CharField(max_length=20, default='B+ (67 pts)')

    # Term 2 Subjects & Mean
    t2_math = models.CharField(max_length=10, default='A-')
    t2_eng = models.CharField(max_length=10, default='A')
    t2_kis = models.CharField(max_length=10, default='B+')
    t2_history = models.CharField(max_length=10, default='A-')
    t2_cre = models.CharField(max_length=10, default='A')
    t2_chem = models.CharField(max_length=10, default='A-')
    t2_bio = models.CharField(max_length=10, default='A')
    t2_mean = models.CharField(max_length=20, default='A- (72 pts)')

    # Term 3 Subjects & Mean
    t3_math = models.CharField(max_length=10, default='A')
    t3_eng = models.CharField(max_length=10, default='A')
    t3_kis = models.CharField(max_length=10, default='A-')
    t3_history = models.CharField(max_length=10, default='A')
    t3_cre = models.CharField(max_length=10, default='A')
    t3_chem = models.CharField(max_length=10, default='A')
    t3_bio = models.CharField(max_length=10, default='A')
    t3_mean = models.CharField(max_length=20, default='A (78 pts)')

    # School Fees
    fees_paid = models.CharField(max_length=50, default='Ksh 45,000')
    fees_balance = models.CharField(max_length=50, default='Ksh 5,000')

    def __str__(self):
        return f"{self.adm_number} - {self.first_name} {self.last_name}"