from django.shortcuts import render, redirect
from users.models import User
from django.views import View
from application.forms.create_application_hemis import ApplicationForm, UserForm
from django.contrib import messages
from application.models import Application, ApplicationStatus, BallApplication


class ApplicationCreateView(View):
    def get(self, request):
        user = request.user

        if not user.is_authenticated:
            messages.info(request, "Hemis orqali kiring!")
            return redirect('main:index')
        
        try:
            profile = user.profile
        except User.profile.RelatedObjectDoesNotExist:
            messages.info(request, "Sizning ma'lumotlaringiz topilmadi!")
            return redirect('main:index')
        
        user_form = UserForm(instance=user)
        
        return render(request, 'application/create.html', {
            'user_form': user_form,
        })
        

    def post(self, request):
        form = ApplicationForm(request.POST, request.FILES)
        user = request.user
        student = user.profile

        if Application.objects.filter(student=student).exists():
            messages.info(request, "Siz allaqachon ariza topshirgansiz.")
            return redirect('main:index') 
        
        new_application = Application.objects.create(student=student, application_status=ApplicationStatus.NEW)
        ball_application = BallApplication.objects.create(application=new_application)
        print("Bal xam saqlandi.", ball_application.id)
        

        messages.success(request, "Ariza muvofaqiyatli yuborildi")
        return redirect('main:index') 