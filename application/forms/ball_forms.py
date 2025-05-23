from application.models import BallApplication, SpiritualityBall, TrainingBall, Application
from django import forms


class SpiritualityBallForm(forms.ModelForm):
    class Meta:
        model = SpiritualityBall
        fields = ['field1', 'field2', 'field3', 'field4', 'field5',
                  'field6', 'field7', 'field8', 'field9', 'field10']
 

class TrainingBallForm(forms.ModelForm):
    class Meta:
        model = TrainingBall
        fields = ['field']
        
    
class SpecialForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['application_status']
