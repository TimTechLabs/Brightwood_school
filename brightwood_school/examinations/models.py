from django.db import models
from students.models import StudentProfile

class StudentReport(models.Model):
    TERM_CHOICES = [
        ('Term 1', 'Term 1'),
        ('Term 2', 'Term 2'),
        ('Term 3', 'Term 3'),
    ]

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='reports')
    term = models.CharField(max_length=20, choices=TERM_CHOICES, default='Term 1')
    
    # 5 Subject Marks (0 - 100)
    maths = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    kiswahili = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    
    # Subject Grades (Auto-calculated)
    maths_grade = models.CharField(max_length=2, blank=True)
    english_grade = models.CharField(max_length=2, blank=True)
    kiswahili_grade = models.CharField(max_length=2, blank=True)
    chemistry_grade = models.CharField(max_length=2, blank=True)
    biology_grade = models.CharField(max_length=2, blank=True)
    
    # Overall Performance
    mean_score = models.FloatField(blank=True, null=True)
    mean_grade = models.CharField(max_length=2, blank=True)

    class Meta:
        unique_together = ('student', 'term')

    def calculate_grade(self, score):
        if score >= 80:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'E'

    def save(self, *args, **kwargs):
        # Calculate subject grades
        self.maths_grade = self.calculate_grade(self.maths)
        self.english_grade = self.calculate_grade(self.english)
        self.kiswahili_grade = self.calculate_grade(self.kiswahili)
        self.chemistry_grade = self.calculate_grade(self.chemistry)
        self.biology_grade = self.calculate_grade(self.biology)
        
        # Calculate mean score and mean grade
        total = self.maths + self.english + self.kiswahili + self.chemistry + self.biology
        self.mean_score = round(total / 5.0, 2)
        self.mean_grade = self.calculate_grade(self.mean_score)
        
        super().save(*args, **kwargs)

def __str__(self):
    return f"{self.student.admission_number} - {self.term}"