from django.contrib import admin
from .models import Attendance
from django.contrib import admin
# Only register custom models if you have any here
admin.site.register(Attendance)