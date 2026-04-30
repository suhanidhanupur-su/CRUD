# from django.contrib import admin
# from django.urls import path,include


# urlpatterns = [

# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('students', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('edit/<int:id>/', edit_student, name='edit_student'),]
