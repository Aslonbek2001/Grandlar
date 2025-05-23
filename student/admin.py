from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['user', 'student_id_number', 'passport_number', 'gpa']


admin.site.register(Student, StudentAdmin)
