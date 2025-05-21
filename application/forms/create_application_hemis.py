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
        fields = ['full_name', 'address']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


class StudentForm(forms.ModelForm):
    user = UserForm()  # UserFormni StudentFormga bog'lash

    class Meta:
        model = Student
        fields = ['user', 'student_id_number', 'image', 'passport_number', 'gpa', 
                  'specialty', 'studentStatus', 'educationForm',  
                  'group', 'level', 'semester']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

class ApplicationForm(forms.ModelForm):
    student = StudentForm()
    class Meta:
        model = Application
        fields = ['student', 'application_status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].disabled = True

        
    
  