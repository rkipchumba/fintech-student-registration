from django import forms
from .models import Student, ClassStream

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'class_stream']

class ClassStreamForm(forms.ModelForm):
    class Meta:
        model = ClassStream
        fields = ['name']