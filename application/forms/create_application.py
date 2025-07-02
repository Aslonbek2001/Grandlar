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

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
                'reading_culture', 
                'five_initiatives', 
                'manners', 
                'participation_in_events', 
                'attendance', 
                'enlightenment_classes', 
                'volunteer_work', 
                'cultural_visits', 
                'sports_activity', 
                'spiritual_enlightenment'
            ]

        widgets = {
            field: forms.FileInput(attrs={'class': 'form-control'})
            for field in fields
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
 

        
    
  
    # widgets = {
    #         'reading_culture': forms.FileInput(attrs={'class': 'form-control'}),
    #         'five_initiatives': forms.FileInput(attrs={'class': 'form-control'}),
    #         'manners': forms.FileInput(attrs={'class': 'form-control'}),
    #         'participation_in_events': forms.FileInput(attrs={'class': 'form-control'}),
    #         'attendance': forms.FileInput(attrs={'class': 'form-control'}),
    #         'enlightenment_classes': forms.FileInput(attrs={'class': 'form-control'}),
    #         'volunteer_work': forms.FileInput(attrs={'class': 'form-control'}),
    #         'cultural_visits': forms.FileInput(attrs={'class': 'form-control'}),
    #         'sports_activity': forms.FileInput(attrs={'class': 'form-control'}),
    #         'spiritual_enlightenment': forms.FileInput(attrs={'class': 'form-control'}),
    #     }