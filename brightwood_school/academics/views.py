# academics/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ClassRoom, Subject
from students.models import Student
from examinations.models import Exam, Mark

@login_required
def school_dashboard_view(request):
    context = {
        'students': Student.objects.all(),
        'classrooms': ClassRoom.objects.all(),
        'subjects': Subject.objects.all(),
        'exams': Exam.objects.all(),
        'marks': Mark.objects.all(),
    }
    return render(request, 'academics/school_directory.html', context)