# attendance/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from students.models import Student
from academics.models import ClassRoom

@login_required
def attendance_list(request):
    attendances = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        classroom_id = request.POST.get('classroom')
        status = request.POST.get('status')
        
        if student_id and classroom_id:
            student = Student.objects.get(id=student_id)
            classroom = ClassRoom.objects.get(id=classroom_id)
            Attendance.objects.create(
                student=student,
                classroom=classroom,
                status=status,
                marked_by=request.user
            )
            return redirect('attendance_list')
            
    students = Student.objects.all()
    classrooms = ClassRoom.objects.all()
    return render(request, 'attendance/mark_attendance.html', {
        'students': students,
        'classrooms': classrooms
    })