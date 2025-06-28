from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from users.models import User
from student.models import Student
from django.views import View
from application.forms.create_application import ApplicationForm
from django.contrib import messages
from application.models import Application, ApplicationStatus, BallApplication, YearlyApplicationWindow
from django.utils import timezone
from application.services.create import ApplicationCreationService
from application.utils import get_course
from application.services.validation import UserValidationService

class ApplicationCreateView(View):

    user_validation_service = UserValidationService()
    create_application_service = ApplicationCreationService()

    def get(self, request):
        student = self.user_validation_service.validate(request)
        application_form = ApplicationForm()
        return render(request, 'application/create.html', {
            'form': application_form,
        })
        

    def post(self, request):
        form = ApplicationForm(request.POST, request.FILES)
        student = self.user_validation_service.validate(request)

        if not isinstance(student, Student):
            return student
        
        if not form.is_valid():
            return render(request, 'application/create.html', {'form': form})
                
        new_application = self.create_application_service.create(request, form)
        messages.success(request, "Ariza muvofaqiyatli yuborildi")
        return redirect('main:index') 
    
