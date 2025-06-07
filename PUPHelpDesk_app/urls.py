from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('student/', views.student_agent, name='student_agent'),
    path('applicant/', views.applicant_agent, name='applicant_agent'),
    path('get-token/<str:user_type>/', views.get_token, name='get_token'),
] 
