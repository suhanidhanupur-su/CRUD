# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        std_name = request.POST.get('name')
        std_roll = request.POST.get('roll')
        std_city = request.POST.get('city')
        std_image = request.FILES.get('image')

        Student.objects.create(
            std_name= std_name,
            std_roll=std_roll,
            std_city=std_city,
            std_image=std_image
        )
        return redirect('student_list')

    return render(request, 'add_student.html')



# in add student       
# std_name = request.POST.get('name')
#         std_roll = request.POST.get('roll')
#         std_city = request.POST.get('city')
#         std_image = request.FILES.get('image')

# left side me jo std_name,std_roll...etc ye sare coloum name h and right side me  request.POST.get('name')..etc these are the name attribute of input tag of html file.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.std_name = request.POST.get('name')
        student.std_roll = request.POST.get('roll')
        student.std_city = request.POST.get('city')

        # Image update only if new image uploaded
        if request.FILES.get('image'):
            student.std_image = request.FILES.get('image')

        student.save()
        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})


from django.shortcuts import redirect, get_object_or_404
from .models import Student

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')