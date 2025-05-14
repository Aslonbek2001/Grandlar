from django.shortcuts import render, redirect
from users.models import User
from django.views import View
from application.forms.create_application_hemis import ApplicationForm, StudentForm, UserForm
from django.contrib import messages

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


        application_form = ApplicationForm(initial={'student': user.profile})
        student_form = StudentForm(instance=user.profile)
        user_form = UserForm(instance=user)
        
        return render(request, 'result/application/application_create.html', {
            'application_form': application_form,
            'student_form': student_form,
            'user_form': user_form
        })
        

    def post(self, request):
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return render(request, template_name='result/index.html',context={'message': "Arizangiz yuborildi."})
        