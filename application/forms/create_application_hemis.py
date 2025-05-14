# Hemis bilan foydalangan xolatda
from django import forms
from application.models import Application
from student.models import Student
from users.models import User
from django.core.validators import RegexValidator

# Telefon raqami validatori
phone_regex = RegexValidator(
    regex=r'^\+?998\d{9}$',
    message="Telefon raqami +998901234567 formatida bo'lishi kerak."
)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'second_name', 'third_name', 
                  'full_name', 'short_name', 'phone', 'address', 'role']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


class StudentForm(forms.ModelForm):
    user = UserForm()  # UserFormni StudentFormga bog'lash

    class Meta:
        model = Student
        fields = ['user', 'student_id_number', 'image', 'passport_number', 'gpa', 
                  'specialty', 'studentStatus', 'educationForm', 'educationType', 
                  'paymentForm', 'group', 'educationLang', 'faculty', 'localityType', 
                  'level', 'semester', 'education_year', 'province', 'district', 
                  'accommodation']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
        


class ApplicationForm(forms.ModelForm):
    student = StudentForm()

    class Meta:
        model = Application
        fields = ['student', 'student_education_direction', 'student_privilege_category', 
                  'student_education_level', 'application_status']
    
  