from django.db import models
from django.conf import settings

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    subject_specialty = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Teacher {self.first_name or ''} {self.last_name or ''}".strip()