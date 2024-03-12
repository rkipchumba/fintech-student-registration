from django.db import models

class ClassStream(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
       return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_stream = models.ForeignKey(ClassStream, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

