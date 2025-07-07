# Hemis bilan foydalangan xolatda
from django import forms
from application.models import Application
from student.models import Student
from users.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

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
    
    def clean(self):
        cleaned_data = super().clean()
        for field in self.Meta.fields:
            file = cleaned_data.get(field)
            if isinstance(file, UploadedFile):  # Faqat yangi yuklangan fayllarni tekshir
                if file.content_type != 'application/pdf':
                    self.add_error(field, "Faqat PDF formatdagi fayl yuklash mumkin.")
                if file.size > 10 * 1024 * 1024:
                    self.add_error(field, "Fayl hajmi 10 MB dan oshmasligi kerak.")
        return cleaned_data
