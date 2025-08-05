from django.shortcuts import render, redirect
from django.views import View
from application.forms.create_application import ApplicationForm
from django.contrib import messages
from application.services.create import ApplicationCreationService
from application.services.validation import UserValidationService, CombinedValidationService
from django.contrib.auth.mixins import LoginRequiredMixin

class ApplicationCreateView(LoginRequiredMixin, View):
    
    def dispatch(self, request, *args, **kwargs):
        self.validation_service = CombinedValidationService()
        self.create_application_service = ApplicationCreationService()

        try:
            self.validation_service.validate(request)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('main:index')

        return super().dispatch(request, *args, **kwargs)

    login_url = 'users:login'
    redirect_field_name = 'next'

    def get(self, request):
        application_form = ApplicationForm()
        return render(request, 'application/create.html', {
            'form': application_form,
        })

    def post(self, request):
        form = ApplicationForm(request.POST, request.FILES)
        if not form.is_valid():
            messages.error(request, "Iltimos, formadagi xatolarni tuzating.")
            return render(request, 'application/create.html', {'form': form})
        
        try:
            self.create_application_service.create(request, form)
            messages.success(request, "Ariza muvofaqiyatli yuborildi")
            return redirect('application:list') 
        except Exception as e:
            messages.error(request, str(e))
            return render(request, 'application/create.html', {'form': form})

        
    
