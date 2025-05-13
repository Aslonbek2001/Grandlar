
# Hemis bilan foydalangan xolatda


from django import forms
from application.models import Application
from django.core.validators import RegexValidator

# Telefon raqami validatori
phone_regex = RegexValidator(
    regex=r'^\+?998\d{9}$',
    message="Telefon raqami +998901234567 formatida bo'lishi kerak."
)



# forms.py
from django import forms
from application.models import Application
from application.choices import PrivilegeCategory, EducationDirection, EducationLevel


class ApplicationForm(forms.ModelForm):
    student_education_direction = forms.ChoiceField(choices=EducationDirection.CHOICES)
    student_privilege_category = forms.ChoiceField(choices=PrivilegeCategory.CHOICES)
    student_education_level = forms.ChoiceField(choices=EducationLevel.CHOICES)

    class Meta:
        model = Application
        fields = [
            'student_education_direction',
            'student_privilege_category',
            'student_education_level',
            'application_status',
        ]

