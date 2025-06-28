from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from application.models import Application
from application.forms.create_application import ApplicationForm 
from application.services.validation import ApplicationValidationService
from application.services.validation import CombinedValidationService, UserValidationService

class ApplicationUpdateView(View):

    validation_service = CombinedValidationService()

    def get(self, request, pk):
        try:
            self.validation_service.validate(request)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('main:index')
        
        application = get_object_or_404(Application, pk=pk, student__user=request.user)


        form = ApplicationForm(instance=application)
        return render(request, 'application/edit.html', {'form': form, 'application': application})

    def post(self, request, pk):
        try:
            self.validation_service.validate(request)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('main:index')
        
        application = get_object_or_404(Application, pk=pk, student__user=request.user)

        form = ApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Ariza muvaffaqiyatli yangilandi.")
            return redirect('application:list')
        return render(request, 'application/edit.html', {'form': form, 'application': application})
