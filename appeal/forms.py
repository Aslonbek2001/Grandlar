from .models import Appeal, AnswerToAppeal
from django import forms

class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ['message_file']
        widgets = {
            'message_file': forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'required': True  # bu shu yerda bo'lishi kerak edi!
        }),
        }
        labels = {
            'message_file': 'Apelatsiya arizasini pdf shaklda yuboring',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message_file'].required = True 

    def clean_message_file(self):
        file = self.cleaned_data.get('message_file')

        if file:
            # 1️⃣ Fayl hajmini tekshirish (6 MB = 6 * 1024 * 1024 bayt)
            max_size = 6 * 1024 * 1024
            if file.size > max_size:
                raise forms.ValidationError("Fayl hajmi 6 MB dan oshmasligi kerak.")

            # 2️⃣ Fayl formatini tekshirish
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError("Faqat PDF formatdagi faylga ruxsat beriladi.")

        return file



class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerToAppeal
        fields = ['answer_text']
        widgets = {
            'answer_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Javobingizni shu yerga yozing...'
            }),
        }
        labels = {
            'answer_text': 'Javob matni',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer_text'].required = True