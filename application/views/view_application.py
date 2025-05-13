from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from application.models import Application
from application.forms.form_application import ApplicationForm

class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application/application_form.html'  
    success_url = reverse_lazy('application:success')

    def form_valid(self, form):
        return super().form_valid(form)
