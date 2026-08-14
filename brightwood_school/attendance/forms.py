# attendance/forms.py
from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'classroom', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'style': 'padding: 0.5rem; width: 100%; border: 1px solid #cbd5e1; border-radius: 6px;'}),
            'student': forms.Select(attrs={'style': 'padding: 0.5rem; width: 100%; border: 1px solid #cbd5e1; border-radius: 6px;'}),
            'classroom': forms.Select(attrs={'style': 'padding: 0.5rem; width: 100%; border: 1px solid #cbd5e1; border-radius: 6px;'}),
            'status': forms.Select(attrs={'style': 'padding: 0.5rem; width: 100%; border: 1px solid #cbd5e1; border-radius: 6px;'}),
        }