# academics/models.py
from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=50, unique=True) # e.g., Form 1, Grade 8
    section = models.CharField(max_length=10, blank=True, null=True) # e.g., A, B, East

    def __str__(self):
        return f"{self.name} {self.section if self.section else ''}"

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"