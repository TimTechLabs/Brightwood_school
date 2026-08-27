from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Import models across apps
from students.models import Student
from academics.models import ClassRoom, Subject
from examinations.models import Exam, Mark
from teachers.models import Teacher
from finance.models import FeePayment  # Update to match your finance model name

@login_required
def school_dashboard_view(request):
    # Optional search query from frontend lookup button/input
    query = request.GET.get('q', '')

    if query:
        students = Student.objects.filter(first_name__icontains=query)
        teachers = Teacher.objects.filter(first_name__icontains=query)
        # Add additional filter logic for exams, finance, etc.
    else:
        students = Student.objects.all()
        teachers = Teacher.objects.all()

    context = {
        'students': students,
        'classrooms': ClassRoom.objects.all(),
        'subjects': Subject.objects.all(),
        'exams': Exam.objects.all(),
        'marks': Mark.objects.all(),
        'teachers': teachers,
        'finance': FeePayment.objects.all(),
    }
    return render(request, 'academics/school_directory.html', context)