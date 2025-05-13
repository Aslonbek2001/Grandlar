
# Hemissiz foydalangan xolatda

from django import forms
from application.models import Application
from django.core.validators import RegexValidator

# Telefon raqami validatori
phone_regex = RegexValidator(
    regex=r'^\+?998\d{9}$',
    message="Telefon raqami +998901234567 formatida bo'lishi kerak."
)

class ApplicationForm(forms.ModelForm):
    student_phone = forms.CharField(
        validators=[phone_regex],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Application
        fields = [
            'student_id',
            'student_name',
            'student_phone',
            'student_address',
            'student_gpa',
            'student_education_direction',
            'student_privilege_category',
            'student_education_level',
            'application_status',
        ]
        exclude = ['application_status']
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'student_gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'student_education_direction': forms.Select(attrs={'class': 'form-select'}),
            'student_privilege_category': forms.Select(attrs={'class': 'form-select'}),
            'student_education_level': forms.Select(attrs={'class': 'form-select'}),
            'application_status': forms.Select(attrs={'class': 'form-select'}),
        }
