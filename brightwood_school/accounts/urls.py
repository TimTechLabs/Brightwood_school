from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.landing_page_view, name='landing'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]