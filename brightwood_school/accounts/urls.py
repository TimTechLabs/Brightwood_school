from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page_view, name='landing'),
    path('dashboard/', views.admin_dashboard_view, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
]