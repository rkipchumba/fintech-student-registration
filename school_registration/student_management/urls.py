from django.urls import path
from .views import class_streams, single_class_stream, create_class_stream, edit_student, delete_student, single_student, all_students

urlpatterns = [
    path('class-streams/', class_streams, name='class_streams'),
    path('class-stream/<int:stream_id>/', single_class_stream, name='single_class_stream'),
    path('create-class-stream/', create_class_stream, name='create_class_stream'),
    path('edit-student/<int:student_id>/', edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', delete_student, name='delete_student'),
    path('single-student/<int:student_id>/', single_student, name='single_student'),
    path('all-students/', all_students, name='all_students'),


]
