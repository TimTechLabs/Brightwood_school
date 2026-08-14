# academics/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('directory/', views.school_dashboard_view, name='school_directory'),
]