from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from application.models import Application
from application.forms.create_application import ApplicationForm 

class ApplicationUpdateView(View):
    def get(self, request, pk):
        application = get_object_or_404(Application, pk=pk, student__user=request.user)

        form = ApplicationForm(instance=application)
        return render(request, 'application/edit.html', {'form': form, 'application': application})

    def post(self, request, pk):
        application = get_object_or_404(Application, pk=pk, student__user=request.user)

        form = ApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Ariza muvaffaqiyatli yangilandi.")
            return redirect('main:index')
        return render(request, 'application/edit.html', {'form': form, 'application': application})
