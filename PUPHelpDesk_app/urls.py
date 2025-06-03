from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('student-help-desk/', views.student_agent, name='student_agent'),
] 
