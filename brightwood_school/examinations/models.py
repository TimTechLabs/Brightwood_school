# examinations/models.py
from django.db import models
from students.models import Student
from academics.models import Subject, ClassRoom

class Exam(models.Model):
    name = models.CharField(max_length=100) # e.g., Term 1 Midterm Exam
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    term = models.CharField(max_length=50) # e.g., Term 1
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.classroom}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    out_of = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)

    class Meta:
        unique_together = ('student', 'exam', 'subject') # Prevent duplicate grades for the same exam subject

    def __str__(self):
        return f"{self.student.admission_number} - {self.subject.name}: {self.score}/{self.out_of}"