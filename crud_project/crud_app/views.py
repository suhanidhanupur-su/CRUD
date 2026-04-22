# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        city = request.POST.get('city')
        image = request.FILES.get('image')

        Student.objects.create(
            std_name=name,
            std_roll=roll,
            std_city=city,
            std_image=image
        )
        return redirect('student_list')

    return render(request, 'add_student.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})