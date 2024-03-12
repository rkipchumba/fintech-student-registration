from django.shortcuts import render, get_object_or_404, redirect
from .models import ClassStream, Student
from .forms import StudentForm, ClassStreamForm

def create_class_stream(request):
    if request.method == 'POST':
        form = ClassStreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_streams')
    else:
        form = ClassStreamForm()
    return render(request, 'create_class_stream.html', {'form': form})

def class_streams(request):
    streams = ClassStream.objects.all()
    return render(request, 'class_streams.html', {'streams': streams})


def single_class_stream(request, stream_id):
    stream = get_object_or_404(ClassStream, id=stream_id)
    students = Student.objects.filter(class_stream=stream)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('single_class_stream', stream_id=stream_id)
    else:
        form = StudentForm()

    return render(request, 'single_class_stream.html', {'stream': stream, 'students': students, 'form': form})



def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('single_class_stream', stream_id=student.class_stream.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {'form': form, 'student': student})

def single_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'single_student.html', {'student': student})

def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html', {'students': students})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    stream_id = student.class_stream.id
    student.delete()
    return redirect('single_class_stream', stream_id=stream_id)