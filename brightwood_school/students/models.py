from django.db import models
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    admission_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    current_class = models.CharField(max_length=50, blank=True, null=True)  # <-- Add this line

    def __str__(self):
        return f"{self.admission_number}" if self.admission_number else "Student Profile"