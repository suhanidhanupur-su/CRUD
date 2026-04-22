# from django.contrib import admin
# from django.urls import path,include


# urlpatterns = [

# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
]